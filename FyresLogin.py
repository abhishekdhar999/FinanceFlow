from fyers_apiv3 import fyersModel
import pandas as pd
import datetime as dt
import time
import numpy as np
import webbrowser
from datetime import datetime,timedelta
from fyers_apiv3.FyersWebsocket import data_ws


# Fyers API credentials
client_id = "NDCNXRQC27-100"
secret_key = "6EMN8CYX6L"
redirect_uri = "https://trade.fyers.in/api-login/redirect-uri/index.html"
response_type = "code"
grant_type = "authorization_code"

# Initialize session
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type,
    grant_type=grant_type
)

# Generate the auth code using the session model
response = session.generate_authcode()
print(response)
auth_code = input("Enter the auth code: ")

# Set the authorization code in the session object
session.set_token(auth_code)
response = session.generate_token()
print(response)
access_token = response["access_token"]

# Initialize the FyersModel instance with your client_id and access_token
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token)

# Fetching data
symbol = 'NSE:NIFTYBANK-INDEX'
interval = '1'
start_date = int((datetime.now() - timedelta(days=2)).timestamp())
end_date = int(datetime.now().timestamp())

data = {
    "symbol": symbol,
    "resolution": interval,
    "date_format": "0",
    "range_from": start_date,
    "range_to": end_date,
    "cont_flag": "1"
}

response = fyers.history(data)
ohlc_data = response['candles']

# Convert to DataFrame
columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
df = pd.DataFrame(ohlc_data, columns=columns)
df['date'] = pd.to_datetime(df['timestamp'], unit='s')
df.set_index('date', inplace=True)
df.drop(columns=['timestamp'], inplace=True)

# Calculate brick size
brick_size = round(df['open'].iloc[0] / 2000)

# Generate Renko bricks
def generate_renko_bricks(df, brick_size):
    renko_bricks = []
    previous_close = df['close'].iloc[0]

    for i in range(len(df)):
        while True:
            if df['close'].iloc[i] >= previous_close + brick_size:
                previous_close += brick_size
                renko_bricks.append(previous_close)
            elif df['close'].iloc[i] <= previous_close - brick_size:
                previous_close -= brick_size
                renko_bricks.append(previous_close)
            else:
                break

    return renko_bricks

renko_bricks = generate_renko_bricks(df, brick_size)

# Create a DataFrame for Renko bricks
renko_df = pd.DataFrame({'close': renko_bricks})
renko_df.index = pd.date_range(start=df.index[0], periods=len(renko_bricks), freq='min')

# Calculate Donchian Channels
def calculate_donchian_channels(renko_df, period=20):
    renko_df['donchian_high'] = renko_df['close'].rolling(window=period).max()
    renko_df['donchian_low'] = renko_df['close'].rolling(window=period).min()
    return renko_df

renko_df = calculate_donchian_channels(renko_df)

# Generate Buy Signals
# Generate Buy Signals
def generate_buy_signals(renko_df):
    # Initialize buy signals with 0s
    buy_signals = [0] * len(renko_df)
    
    for i in range(1, len(renko_df)):
        if renko_df['close'].iloc[i] > renko_df['donchian_high'].iloc[i - 1]:
            buy_signals[i] = 1  # Buy signal
        elif renko_df['close'].iloc[i] < renko_df['donchian_low'].iloc[i - 1]:
            buy_signals[i] = 0  # No signal
        else:
            buy_signals[i] = buy_signals[i - 1]  # Carry forward last signal

    renko_df['buy_signal'] = buy_signals
    return renko_df

renko_df = generate_buy_signals(renko_df)
print(renko_df[['close', 'donchian_high', 'donchian_low', 'buy_signal']])

symbol = 'NSE:NIFTYBANK'
quote_data = fyers.quotes(symbol)
print("quotedata",quote_data)
# Extract the current market price
# current_market_price = quote_data['d']['data'][0]['last_price']
# print(f"Current Market Price: {current_market_price}")

limit_price = 0.0025 #max(current_market_price, 0.0025)
# def place_order(symbol, qty=1):
Odata = {
        "symbol": 'NSE:NIFTYIETF-EQ',
        "qty": 1,
        "type": 1,  # 1 for Market order
        "side": 1,  # 1 for Buy
        "productType": "INTRADAY",
        "limitPrice": 0,
        "stopPrice": 0,
        "disclosedQty": 0,
        "validity": "DAY"
    }
    
    # response = fyers.place_order(order_data)
    # print("Order Response:", response)

response = fyers.place_order(Odata)
print("order palced",response)
# Check for buy signals and place an order
# if renko_df['buy_signal'].iloc[0] == 1:
#     place_order(symbol="NSE:NIFTYBANK-INDEX", qty=1)

# Display the final Renko DataFrame with signals


output_file = 'nifty_bank_analysis.xlsx'

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    renko_df.to_excel(writer, sheet_name='Renko Data')
    # Add other DataFrames if needed
    # df.to_excel(writer, sheet_name='Original Data')
    # signals.to_excel(writer, sheet_name='Signals')

print(f"Data has been saved to {output_file}")

# # REQUIREMENT:
# # I MIN KA DATA hist 2-day for nifty bank take ohlc uske basis pe ranko bricks generate 
# # ranko kla size = market ka open price/2000
# # no ayega usko convert krna ha decimal hatake pure no mai vo hogya brick size utne price hoga brick ki size= point ki brick hui poore din ki bricks
# # fir dolchian ranko ki last 20 brcik ma lowest price aur highest ye range ha 
# # dolxhian valuw har min change hogi 
# # dolchian channel k high se 1 brick bar bnti ha agr o k upar to buy signal agr 1 brick neeche jata ha dolcj=hian k lowest se to buy pe signal triger hona chaiye
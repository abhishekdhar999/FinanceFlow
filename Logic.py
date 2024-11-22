import pandas as pd

# Sample data
data = [
    {'ltp': 52580.5, 'prev_close_price': 51703.95, 'ch': 876.55, 'chp': 1.7, 'exch_feed_time': 1719308652, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52578.1, 'prev_close_price': 51703.95, 'ch': 874.15, 'chp': 1.69, 'exch_feed_time': 1719308653, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52584.5, 'prev_close_price': 51703.95, 'ch': 880.55, 'chp': 1.7, 'exch_feed_time': 1719308653, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52577.25, 'prev_close_price': 51703.95, 'ch': 873.3, 'chp': 1.69, 'exch_feed_time': 1719308654, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52585.05, 'prev_close_price': 51703.95, 'ch': 881.1, 'chp': 1.7, 'exch_feed_time': 1719308654, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52584.1, 'prev_close_price': 51703.95, 'ch': 880.15, 'chp': 1.7, 'exch_feed_time': 1719308655, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52589.7, 'prev_close_price': 51703.95, 'ch': 885.75, 'chp': 1.71, 'exch_feed_time': 1719308655, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52588.45, 'prev_close_price': 51703.95, 'ch': 884.5, 'chp': 1.71, 'exch_feed_time': 1719308656, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52599.15, 'prev_close_price': 51703.95, 'ch': 895.2, 'chp': 1.73, 'exch_feed_time': 1719308656, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52599.3, 'prev_close_price': 51703.95, 'ch': 895.35, 'chp': 1.73, 'exch_feed_time': 1719308657, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52597.1, 'prev_close_price': 51703.95, 'ch': 893.15, 'chp': 1.73, 'exch_feed_time': 1719308657, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52595.5, 'prev_close_price': 51703.95, 'ch': 891.55, 'chp': 1.72, 'exch_feed_time': 1719308658, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52598.0, 'prev_close_price': 51703.95, 'ch': 894.05, 'chp': 1.73, 'exch_feed_time': 1719308658, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52599.9, 'prev_close_price': 51703.95, 'ch': 895.95, 'chp': 1.73, 'exch_feed_time': 1719308659, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52605.0, 'prev_close_price': 51703.95, 'ch': 901.05, 'chp': 1.74, 'exch_feed_time': 1719308659, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52603.7, 'prev_close_price': 51703.95, 'ch': 899.75, 'chp': 1.74, 'exch_feed_time': 1719308660, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52593.9, 'prev_close_price': 51703.95, 'ch': 889.95, 'chp': 1.72, 'exch_feed_time': 1719308660, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52597.5, 'prev_close_price': 51703.95, 'ch': 893.55, 'chp': 1.73, 'exch_feed_time': 1719308661, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52600.2, 'prev_close_price': 51703.95, 'ch': 896.25, 'chp': 1.73, 'exch_feed_time': 1719308661, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52605.1, 'prev_close_price': 51703.95, 'ch': 901.15, 'chp': 1.74, 'exch_feed_time': 1719308662, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52610.3, 'prev_close_price': 51703.95, 'ch': 906.35, 'chp': 1.75, 'exch_feed_time': 1719308662, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52608.65, 'prev_close_price': 51703.95, 'ch': 904.7, 'chp': 1.75, 'exch_feed_time': 1719308663, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52606.55, 'prev_close_price': 51703.95, 'ch': 902.6, 'chp': 1.75, 'exch_feed_time': 1719308663, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52608.6, 'prev_close_price': 51703.95, 'ch': 904.65, 'chp': 1.75, 'exch_feed_time': 1719308664, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52604.95, 'prev_close_price': 51703.95, 'ch': 900.9, 'chp': 1.74, 'exch_feed_time': 1719308664, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52601.15, 'prev_close_price': 51703.95, 'ch': 897.2, 'chp': 1.73, 'exch_feed_time': 1719308665, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52598.55, 'prev_close_price': 51703.95, 'ch': 894.6, 'chp': 1.73, 'exch_feed_time': 1719308665, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52597.95, 'prev_close_price': 51703.95, 'ch': 894.0, 'chp': 1.73, 'exch_feed_time': 1719308666, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52603.35, 'prev_close_price': 51703.95, 'ch': 899.4, 'chp': 1.74, 'exch_feed_time': 1719308666, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52605.65, 'prev_close_price': 51703.95, 'ch': 901.7, 'chp': 1.74, 'exch_feed_time': 1719308667, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52602.85, 'prev_close_price': 51703.95, 'ch': 898.9, 'chp': 1.74, 'exch_feed_time': 1719308667, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52598.85, 'prev_close_price': 51703.95, 'ch': 894.9, 'chp': 1.73, 'exch_feed_time': 1719308668, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52604.0, 'prev_close_price': 51703.95, 'ch': 900.05, 'chp': 1.74, 'exch_feed_time': 1719308668, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52606.6, 'prev_close_price': 51703.95, 'ch': 902.65, 'chp': 1.75, 'exch_feed_time': 1719308669, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52604.55, 'prev_close_price': 51703.95, 'ch': 900.6, 'chp': 1.74, 'exch_feed_time': 1719308669, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52606.1, 'prev_close_price': 51703.95, 'ch': 902.15, 'chp': 1.75, 'exch_feed_time': 1719308670, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52603.4, 'prev_close_price': 51703.95, 'ch': 899.45, 'chp': 1.74, 'exch_feed_time': 1719308670, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52602.95, 'prev_close_price': 51703.95, 'ch': 899.0, 'chp': 1.74, 'exch_feed_time': 1719308671, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52603.25, 'prev_close_price': 51703.95, 'ch': 899.3, 'chp': 1.74, 'exch_feed_time': 1719308671, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52602.65, 'prev_close_price': 51703.95, 'ch': 898.7, 'chp': 1.74, 'exch_feed_time': 1719308672, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52602.0, 'prev_close_price': 51703.95, 'ch': 898.05, 'chp': 1.74, 'exch_feed_time': 1719308672, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52601.8, 'prev_close_price': 51703.95, 'ch': 897.85, 'chp': 1.73, 'exch_feed_time': 1719308673, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52598.9, 'prev_close_price': 51703.95, 'ch': 894.95, 'chp': 1.73, 'exch_feed_time': 1719308673, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52604.4, 'prev_close_price': 51703.95, 'ch': 900.45, 'chp': 1.74, 'exch_feed_time': 1719308674, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52604.95, 'prev_close_price': 51703.95, 'ch': 901.0, 'chp': 1.74, 'exch_feed_time': 1719308674, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52603.35, 'prev_close_price': 51703.95, 'ch': 899.4, 'chp': 1.74, 'exch_feed_time': 1719308675, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52605.4, 'prev_close_price': 51703.95, 'ch': 901.45, 'chp': 1.74, 'exch_feed_time': 1719308675, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52605.55, 'prev_close_price': 51703.95, 'ch': 901.6, 'chp': 1.74, 'exch_feed_time': 1719308676, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52602.1, 'prev_close_price': 51703.95, 'ch': 898.15, 'chp': 1.74, 'exch_feed_time': 1719308676, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52605.5, 'prev_close_price': 51703.95, 'ch': 901.55, 'chp': 1.74, 'exch_feed_time': 1719308677, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'},
    {'ltp': 52603.9, 'prev_close_price': 51703.95, 'ch': 899.95, 'chp': 1.74, 'exch_feed_time': 1719308677, 'high_price': 52669.3, 'low_price': 51747.65, 'open_price': 51759.45, 'type': 'if', 'symbol': 'NSE:NIFTYBANK-INDEX'}
]

# Step 1: Create DataFrame and convert column names to lowercase
df = pd.DataFrame(data)
df.columns = [col.lower() for col in df.columns]
print("df",df)
# Step 2: Parse dates and set the date column as the index
df['date'] = pd.to_datetime(df['exch_feed_time'], unit='s')
df.set_index('date', inplace=True)
print("df-after",df)
# Step 3: Extract unique dates
unique_dates = df.index.normalize().unique()
print("uniquedate",unique_dates)
# Step 4: Calculate brick sizes based on the open price at 9:15 AM
brick_sizes = {}
for unique_date in unique_dates:
    daily_data = df.between_time('09:35', '09:50')
    print("daily_data",daily_data)
    if not daily_data.empty:
        open_price = daily_data.loc[daily_data.index.normalize() == unique_date, 'ltp'].iloc[0]
        print("open_price",open_price)
        brick_sizes[unique_date] = round(open_price / 2000)

# Step 5: Map the brick sizes to the original dataframe
df['renko_size'] = df.index.normalize().map(brick_sizes)
print("df-afterranko",df)
# Step 6: Generate Renko bricks manually
def generate_renko(df, brick_sizes):
    renko_bricks = []
    renko_dates = []
    previous_close = df['ltp'].iloc[0]
    for i in range(1, len(df)):
        date = df.index[i]
        print("date",date)
        brick_size = brick_sizes.get(date.normalize())
        print("brick_size",brick_size)
        if brick_size is not None:
            brick_count = abs(df['ltp'].iloc[i] - previous_close) // brick_size
            if brick_count > 0:
                direction = 1 if df['ltp'].iloc[i] > previous_close else -1
                previous_close += direction * brick_size * brick_count
                renko_bricks.append(previous_close)
                renko_dates.append(date)
    renko_df = pd.DataFrame({'date': renko_dates, 'close': renko_bricks})
    renko_df.set_index('date', inplace=True)
    return renko_df

# Generate Renko bricks
renko_df = generate_renko(df, brick_sizes)
print("renkodf",renko_df)
# Step 7: Calculate Donchian Channels
donchian_period = 20
renko_df['donchian_high'] = renko_df['close'].rolling(window=donchian_period).max()
renko_df['donchian_low'] = renko_df['close'].rolling(window=donchian_period).min()
renko_df['donchian_mid'] = (renko_df['donchian_high'] + renko_df['donchian_low']) / 2
print("renko after donchian",renko_df)
# Step 8: Generate Buy and Sell Signals
def generate_signals(df, donchian_period=20):
    signals = pd.DataFrame(index=df.index)
    signals['cumulative_move'] = 0.0
    signals['buy'] = 0
    signals['sell'] = 0
    signals['position'] = 0

    cumulative_move = 0.0
    for i in range(1, len(df)):
        price_move = df['close'].iloc[i] - df['close'].iloc[i - 1]
        cumulative_move += price_move

        if cumulative_move > 0 and df['close'].iloc[i] > df['donchian_high'].iloc[i - 1]:
            signals['buy'].iloc[i] = 1
            signals['position'].iloc[i] = 1
            cumulative_move = 0

        elif cumulative_move < 0 and df['close'].iloc[i] < df['donchian_low'].iloc[i - 1]:
            signals['sell'].iloc[i] = 1
            signals['position'].iloc[i] = -1
            cumulative_move = 0

        signals['cumulative_move'].iloc[i] = cumulative_move

        if signals['buy'].iloc[i] == 0 and signals['sell'].iloc[i] == 0:
            signals['position'].iloc[i] = signals['position'].iloc[i - 1]

    return signals

# Generate signals
signals = generate_signals(renko_df)
print("signals",signals)
# Step 9: Combine data into a single DataFrame
combined_df = renko_df.join(signals)

print("combine df",combined_df)

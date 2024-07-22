#We'll load these files into Pandas Dataframefor processing

import pandas as pd
import os

DATA_DIR = "/path/to/your/2019/csv/files/"
csv_files = [file for file in os.listdir(DATA_DIR) if file.endswith('.csv')]
dfs = []
for file in csv_files:
    file_path = os.path.join(DATA_DIR, file)
    df = pd.read_csv(file_path, parse_dates=['pickup_datetime', 'dropoff_datetime'])
    dfs.append(df)

taxi_df = pd.concat(dfs, ignore_index=True)
print(taxi_df.head())

#We'll clean the data by removing trips with missing or corrupt data, and we'll derive new columns for trip duration and average speed.

taxi_df.dropna(inplace=True)
taxi_df = taxi_df[(taxi_df['trip_distance'] > 0) & (taxi_df['trip_duration_minutes'] > 0)]
taxi_df['trip_duration_minutes'] = (taxi_df['dropoff_datetime'] - taxi_df['pickup_datetime']).dt.total_seconds() / 60
taxi_df['average_speed_mph'] = taxi_df['trip_distance'] / (taxi_df['trip_duration_minutes'] / 60)

print(taxi_df.describe())

#Aggregate the data to calculate total trips and average fare per day.

daily_summary = taxi_df.groupby(taxi_df['pickup_datetime'].dt.date)['fare_amount'].agg(['count', 'mean']).reset_index()
daily_summary.columns = ['pickup_date', 'total_trips', 'avg_fare_amount']
print(daily_summary.head())

import sqlite3
import os
import pandas as pd

DB_FILE = "/path/to/your/database.db"

def create_trips_table(conn):
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS trips (
            trip_id INTEGER PRIMARY KEY AUTOINCREMENT,
            pickup_datetime TEXT,
            dropoff_datetime TEXT,
            trip_distance REAL,
            fare_amount REAL,
            passenger_count INTEGER,
            trip_duration_minutes REAL,
            average_speed_mph REAL
        );
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def insert_into_trips_table(conn, df):
    insert_sql = """
        INSERT INTO trips (pickup_datetime, dropoff_datetime, trip_distance, fare_amount,
                           passenger_count, trip_duration_minutes, average_speed_mph)
        VALUES (?, ?, ?, ?, ?, ?, ?);
    """
    try:
        c = conn.cursor()
        # Iterate through each row in the DataFrame and insert into SQLite table
        for index, row in df.iterrows():
            c.execute(insert_sql, (
                row['pickup_datetime'].strftime('%Y-%m-%d %H:%M:%S'),
                row['dropoff_datetime'].strftime('%Y-%m-%d %H:%M:%S'),
                row['trip_distance'],
                row['fare_amount'],
                row['passenger_count'],
                row['trip_duration_minutes'],
                row['average_speed_mph']
            ))
        conn.commit()
        print("Data inserted successfully into SQLite database.")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

CLEANED_DATA_CSV = "/path/to/your/cleaned_data.csv"

cleaned_df = pd.read_csv(CLEANED_DATA_CSV, parse_dates=['pickup_datetime', 'dropoff_datetime'])

# Connect to SQLite database
conn = sqlite3.connect(DB_FILE)

create_trips_table(conn)

insert_into_trips_table(conn, cleaned_df)

# Close the connection
conn.close()

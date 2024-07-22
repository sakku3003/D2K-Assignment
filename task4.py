 # Create visualizations using Matplotlib and Seaborn.
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DB_FILE = "/path/to/your/database.db"

def execute_query(query):
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

query_peak_hours = """
    SELECT 
        strftime('%H', pickup_datetime) AS pickup_hour,
        COUNT(*) AS num_trips
    FROM 
        trips
    GROUP BY 
        pickup_hour
    ORDER BY 
        num_trips DESC
    LIMIT 5;
"""
df_peak_hours = execute_query(query_peak_hours)

plt.figure(figsize=(10, 6))
sns.barplot(x='pickup_hour', y='num_trips', data=df_peak_hours, palette='viridis')
plt.title('Peak Hours for Taxi Usage')
plt.xlabel('Pickup Hour')
plt.ylabel('Number of Trips')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

query_passenger_fare = """
    SELECT 
        passenger_count,
        AVG(fare_amount) AS avg_fare
    FROM 
        trips
    GROUP BY 
        passenger_count
    ORDER BY 
        passenger_count;
"""
df_passenger_fare = execute_query(query_passenger_fare)

plt.figure(figsize=(8, 6))
sns.barplot(x='passenger_count', y='avg_fare', data=df_passenger_fare, palette='muted')
plt.title('Passenger Count vs. Average Trip Fare')
plt.xlabel('Number of Passengers')
plt.ylabel('Average Fare ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

query_monthly_trips = """
    SELECT 
        strftime('%m', pickup_datetime) AS pickup_month,
        COUNT(*) AS num_trips
    FROM 
        trips
    GROUP BY 
        pickup_month
    ORDER BY 
        pickup_month;
"""
df_monthly_trips = execute_query(query_monthly_trips)

plt.figure(figsize=(10, 6))
sns.lineplot(x='pickup_month', y='num_trips', data=df_monthly_trips, marker='o', color='b')
plt.title('Trends in Taxi Usage Over the Year')
plt.xlabel('Month')
plt.ylabel('Number of Trips')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.tight_layout()
plt.show()

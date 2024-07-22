SQL QUERIES

1) Peak hours for taxi usage:
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

2) Passenger Count vs. Trip Fare Analysis:
SELECT 
    passenger_count,
    AVG(fare_amount) AS avg_fare
FROM 
    trips
GROUP BY 
    passenger_count
ORDER BY 
    passenger_count;

3) Trends in Usage Over the Year:
SELECT 
    strftime('%m', pickup_datetime) AS pickup_month,
    COUNT(*) AS num_trips
FROM 
    trips
GROUP BY 
    pickup_month
ORDER BY 
    pickup_month;



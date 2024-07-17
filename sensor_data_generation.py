import random
import time

def sensor_data_generation():
    temperature = round(random.uniform(20.0, 30.0), 2)  # Simulate temperature between 20 and 30 degrees Celsius
    humidity = round(random.uniform(30.0, 70.0), 2)     # Simulate humidity between 30% and 70%
    soil_moisture = round(random.uniform(200, 800), 2)  # Simulate soil moisture levels
    return temperature, humidity, soil_moisture

while True:
    temp, hum, soil = sensor_data_generation()
    print(f"Temperature: {temp} °C, Humidity: {hum} %, Soil Moisture: {soil}")
    time.sleep(2)  # Update every 2 seconds

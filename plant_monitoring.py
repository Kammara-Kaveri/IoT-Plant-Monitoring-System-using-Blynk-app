import platform
import os
import time
import psutil
import BlynkLib
import random
import requests
import platform

# Blynk Auth Token
BLYNK_AUTH = "G5GjwBdZUu5Nvoz_le4iswzZ1VVyb77u"

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Virtual pins for Blynk widgets
TEMP_VPIN = 1
HUMIDITY_VPIN = 2
MOISTURE_VPIN = 3
PUMP_VPIN = 4

# Function to simulate temperature sensor data
def get_temperature():
    return round(random.uniform(20.0, 30.0), 2)

# Function to simulate humidity sensor data
def get_humidity():
    return round(random.uniform(40.0, 60.0), 2)

# Function to simulate soil moisture sensor data
def get_moisture():
    return round(random.uniform(30.0, 70.0), 2)

# Function to control the water pump
@blynk.handle_event('write V{}'.format(PUMP_VPIN))
def water_pump(pin, value):
    if int(value[0]) == 1:
        print("Pump turned ON")
    else:
        print("Pump turned OFF")

# Main loop to send data to Blynk
while True:
    temperature = get_temperature()
    humidity = get_humidity()
    moisture = get_moisture()

    blynk.virtual_write(TEMP_VPIN, temperature)
    blynk.virtual_write(HUMIDITY_VPIN, humidity)
    blynk.virtual_write(MOISTURE_VPIN, moisture)

    print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Moisture: {moisture}%")

    blynk.run()
    time.sleep(2)

#
# RabbitMQ Publisher Program
# Connects and publishes sensor data to an MQTT broker (RabbitMQ)
# Written for the AgriApp 2022 Workshop (March 4-5, 2022)
#

# Main libraries:
import pika # Used for MQTT (pip3 install pika)
import smbus2 # Used for interfacing with I2C
import bme280 # Used for reading the bme280 sensor (pip3 install bme280)
import json # Used for json encoding (pip3 install json)
import time # Used for accessing time

# Set MQTT connection variables
username = 'sensor'
password = '123456'
host = 'ccscloud1.dlsu.edu.ph'
port = 5672
queue = 'sensor'

# Set I2C sensor variables
i2c_port = 1
address = 0x76
bus = smbus2.SMBus(i2c_port)

# This device's number or identifier
node = 1


# 1. Initialize

# Set username and password for connecting to RabbitMQ
credentials = pika.PlainCredentials(username, password)

# Set RabbitMQ connection parameters and connect to MQTT broker
connectParams = pika.ConnectionParameters(host=host, port=port, credentials=credentials)
connection = pika.BlockingConnection(connectParams)
channel = connection.channel()

# Set queue (in which 'topic' the listener will subscribe)
channel.queue_declare(queue='sensor')

# Recalibrate bme280 sensor
calibration_params = bme280.load_calibration_params(bus, address)





while 1:
    # Reads bme280 sensor data
    data = bme280.sample(bus, address, calibration_params)
    t = data.temperature
    h = data.humidity
    p = data.pressure
    
    # Encodes data into a json    
    values = {"NODE": node, "T":t, "H":h, "P":p}
    message = json.dumps(values)
    
    # Publishes data to MQTT broker
    channel.basic_publish(exchange='',
                          routing_key='sensor',
                          body=message)
    
    # Just print the message
    print(message)
    
    # Delay for 10 seconds
    time.sleep(10)

connection.close()


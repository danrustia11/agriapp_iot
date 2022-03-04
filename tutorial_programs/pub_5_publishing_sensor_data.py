import smbus2
import bme280
import time
from datetime import datetime
import pika
import json

port = 1
address = 0x76
bus = smbus2.SMBus(port)

username = 'sensor'
password = '123456'
host = 'ccscloud1.dlsu.edu.ph'
port = 5672
queue = 'sensor'

node = 1

credentials = pika.PlainCredentials(username, password) 
connectParams = pika.ConnectionParameters(host=host, port=port, credentials=credentials)
connection = pika.BlockingConnection(connectParams)
channel = connection.channel()
channel.exchange_declare(exchange='sensor', exchange_type='fanout')

calibration_params = bme280.load_calibration_params(bus, address)

while(1):
    data = bme280.sample(bus, address, calibration_params)
    t = data.temperature
    h = data.humidity
    p = data.pressure
    
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    
    ts = time.time()
    
    values = {"NODE": node, "TS": ts, "DT": dt_string, "T":t, "H":h, "P":p}
    message = json.dumps(values)

    channel.basic_publish(exchange='sensor',
                          routing_key='',
                          body=message)
    
    print(message)
    
    time.sleep(2)



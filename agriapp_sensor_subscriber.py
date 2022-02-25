#
# RabbitMQ Subscriber Program
# Connects and listens to an MQTT broker (RabbitMQ)
# to receive data from wireless sensor nodes
# Written for the AgriApp 2022 Workshop (March 4-5, 2022)
#

# Main libraries:
import pika # Used for MQTT (pip3 install pika)
import json # Used for json decoding (pip3 install json)
import mysql.connector # Used for connecting to MySQL (pip3 install mysql-connector-python)

# Other libraries:
import sys  
import os
from datetime import datetime
import time


# Set MQTT connection variables
username = 'sensor'
password = '123456'
host = '172.16.1.10'
port = 5672
queue = 'sensor'

# Set MySQL variables
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="agriapp_data"
)
table_name = "sensor_data"
mycursor = mydb.cursor()

# Set which node you want to listen to
target_node = 5



# Define a routine called "main"
def main():
    
    # Set username and password for connecting to RabbitMQ
    credentials = pika.PlainCredentials(username, password)
    
    # Set RabbitMQ connection parameters and connect to MQTT broker
    connectParams = pika.ConnectionParameters(host=host, port=port, credentials=credentials)
    connection = pika.BlockingConnection(connectParams)
    channel = connection.channel()
    
    # Set queue (in which 'topic' the listener will subscribe)
    channel.queue_declare(queue=queue)


    # Set a callback (an event that will happen after a message has been received)
    def callback(ch, method, properties, body):
        # Decode 'body' into a json variable
        json_data = json.loads(body)
        
        # Get individual data by json['key']
        node = json_data['NODE']
        t = json_data['T']
        h = json_data['H']
        p = json_data['P']    
        

        
        # Check only data from target_node
        if node == target_node:
            print("[RX]: {}".format(body))
            # Get the date/time in string format
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            
            # Get the date/time in unix format
            ts = time.time()
            
            # Saves data to the database
            sql = "INSERT INTO {} (ID, TIMESTAMP, DATETIME, NODE, TYPE, VALUE) VALUES (NULL, {}, '{}', '{}', '{}', {})".format(table_name, ts, dt_string, node, "T", t)
            mycursor.execute(sql)
            sql = "INSERT INTO {} (ID, TIMESTAMP, DATETIME, NODE, TYPE, VALUE) VALUES (NULL, {}, '{}', '{}', '{}', {})".format(table_name, ts, dt_string, node, "H", h)
            mycursor.execute(sql)
            sql = "INSERT INTO {} (ID, TIMESTAMP, DATETIME, NODE, TYPE, VALUE) VALUES (NULL, {}, '{}', '{}', '{}', {})".format(table_name, ts, dt_string, node, "P", p)
            mycursor.execute(sql)
            
            # Apply changes to the database
            mydb.commit()
            
        
        
    
    channel.basic_consume(queue='sensor', on_message_callback=callback, auto_ack=True)
    
    # Just print waiting for messages
    print('[WAITING] To exit press CTRL+C')
    
    # Starts listening for data
    channel.start_consuming()



# Enter program routine
if __name__ == '__main__':
    # Does the "main" routine"
    try:
        main()
    # Program stops when a keyboard interrupt is detected such as CTRL+C
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)



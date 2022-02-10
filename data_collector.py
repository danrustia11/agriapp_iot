# Import the required libraries
import mysql.connector
import smbus2
import bme280
import time
from datetime import datetime

# Sets up an object for connecting to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="sensor_data"
)
table_name = "agriapp_data"
mycursor = mydb.cursor()


# Sensor variables
port = 1
address = 0x76
bus = smbus2.SMBus(port)
record_delay = 30


# Re-calibrates the BME280 for new measurements
calibration_params = bme280.load_calibration_params(bus, address)




while 1:
    # Reads data from sensor
    data = bme280.sample(bus, address, calibration_params)
    t = round(data.temperature, 2)
    h = round(data.humidity, 2)
    p = round(data.pressure, 2)
    
    # Get the date/time in string format
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Get the date/time in unix format
    ts = time.time()
    
    
    # Stores data to the database
    sql = "INSERT INTO {} (ID, TIMESTAMP, DATETIME, TYPE, VALUE) VALUES (NULL, {}, '{}', '{}', {})".format(table_name, ts, dt_string, "T", t)
    mycursor.execute(sql)
    sql = "INSERT INTO {} (ID, TIMESTAMP, DATETIME, TYPE, VALUE) VALUES (NULL, {}, '{}', '{}', {})".format(table_name, ts, dt_string, "H", h)
    mycursor.execute(sql)
    sql = "INSERT INTO {} (ID, TIMESTAMP, DATETIME, TYPE, VALUE) VALUES (NULL, {}, '{}', '{}', {})".format(table_name, ts, dt_string, "P", p)
    mycursor.execute(sql)

    # Apply changes to the database
    mydb.commit()
    
    
    # Print out the results
    print("T(*C)=", t, " H(%)=", h, " P(kpa)=", p)
    
    # Sets a little delay between readings
    time.sleep(record_delay)



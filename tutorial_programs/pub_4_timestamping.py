import smbus2
import bme280
import time
from datetime import datetime

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

while(1):
    data = bme280.sample(bus, address, calibration_params)
    t = data.temperature
    h = data.humidity
    p = data.pressure
    
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    
    ts = time.time()

    print(ts, dt_string, "T(*C)=", t, " H(%)=", h, "P(hpa)=", p)
    
    time.sleep(2)


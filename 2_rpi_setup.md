The following steps are only required if you would like to setup your own
Raspberry Pi. The RPis provided in this workshop are already set with the steps eblow.

1. Install i2c tools and pip: <br/>

   ```bash
   sudo apt-get install i2c-tools python-pip   # Install i2c tools and pip
   ```

2. Install Python libraries: <br/>
   ```bash
   pip3 install RPi.bme280                 # Installs bme280 library
   pip3 install mysql-connector-python     # Installs mysql library
   pip3 install smbus2                     # Installs smbus2 library
   ```

# test
# program to read BME280
# see https://pypi.org/project/adafruit-circuitpython-bme280/


import time
import board

from adafruit_bme280 import basic as adafruit_bme280


class ReadBme(object):
    def __init__(self):
        # Create sensor object, using the board's default I2C bus.
        i2c = board.I2C()   # uses board.SCL and board.SDA
        self.bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

        # change this to match the location's pressure (hPa) at sea level
        #for basel 1024
        self.bme280.sea_level_pressure = 1028

    def read(self):

        while True:
            print("\nTemperature: %0.1f C" % self.bme280.temperature)
            print("Humidity: %0.1f %%" % self.bme280.relative_humidity)
            print("Pressure: %0.1f hPa" % self.bme280.pressure)
            print("Altitude = %0.2f meters" % self.bme280.altitude)


            time.sleep(2)

        #return {
        #    "temperature": self.bme280.temperature,
        #    "humidity": self.bme280.relative_humidity,
        #   "pressure": self.bme280.pressure,
        #    "altitude": self.bme280.altitude
        #}

if  __name__ == "__main__":
    bme = ReadBme()
    bme.read()
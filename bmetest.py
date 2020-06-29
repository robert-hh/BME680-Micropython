from bme680 import *
from machine import I2C
import time
bme = BME680_I2C(I2C())

for _ in range(3):
    print(bme.temperature, bme.humidity, bme.pressure)
    time.sleep(1)



try: from bme680 import *
except: pass
try: from machine import I2C, Pin
except: pass
from time import sleep

try:
    bme = BME680_I2C(I2C(-1, Pin(13), Pin(12)))

    for _ in range(3):
        print(bme.temperature, bme.humidity, bme.pressure, bme.gas)
        sleep(1)
except:
    print("BME680 not detected")

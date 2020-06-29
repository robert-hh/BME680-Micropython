# Micropython Driver for a BME680 breakout

This a port of an older adafruit driver for use with micropython.org based and
Pycom.io devices using the respecitve MicroPython variant. 

The driver uses the I2C interface. The sensor also supports SPI mode, which is
not supported by this driver yet, but can easily be extended.

Sample usage:

```
from bme680 import *
from machine import I2C
import time
bme = BME680_I2C(I2C())

for _ in range(3):
    print(bme.temperature, bme.humidity, bme.pressure)
    time.sleep(1)
```

## Files:

bme680.py: Drivers using floating point arithmetic  
bme680i.py: Driver using integer arithmentic for the internal calculations according to the BOSCH datasheet. Only for the final result floating point operations are used.
bmetest.py: Sample test script
readme.md: This file
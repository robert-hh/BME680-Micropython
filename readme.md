# Micropython Driver for a BME680 breakout

This a port of an Adafruit driver for use with micropython.org based and
Pycom.io devices using the respecitve MicroPython variant. 

The driver uses the I2C interface. The sensor also supports SPI mode, which is
not supported by this driver yet, but can easily be extended.

Sample usage files:

```
# I2C Interface, genuine Micropython

from bme680 import *
from machine import I2C, Pin
import time
bme = BME680_I2C(I2C(-1, Pin(13), Pin(12)))

for _ in range(3):
    print(bme.temperature, bme.humidity, bme.pressure, bme.gas)
    time.sleep(1)
```

```
# SPI Interface, genuine Micropython

from bme680 import *
from machine import SPI, Pin
import time

cs = Pin(15, Pin.OUT, value=1)
spi = SPI(-1, baudrate=400000, sck=Pin(12), mosi=Pin(13), miso=Pin(14))
bme = BME680_SPI(spi, cs)

for _ in range(3):
    print(bme.temperature, bme.humidity, bme.pressure, bme.gas)
    time.sleep(1)
```

```
# I2C Interface, Pycom devices
# Using the default Pins P9 for sda and P10 for scl

from bme680 import *
from machine import I2C, Pin
import time
cs=Pin("P11", Pin.OUT, value=1)
bme = BME680_I2C(I2C())

for _ in range(3):
    print(bme.temperature, bme.humidity, bme.pressure, bme.gas)
    time.sleep(1)
```

```
# SPI Interface, Pycom devices

from bme680 import *
from machine import SPI, Pin
import time

cs = Pin("P11", Pin.OUT, value=1)
spi = SPI(0, mode=SPI.MASTER, baudrate=400000, pins=("P10", "P9", "P8"))
bme = BME680_SPI(spi, cs)

for _ in range(3):
    print(bme.temperature, bme.humidity, bme.pressure, bme.gas)
    time.sleep(1)
```

## Files:

bme680.py: Drivers using floating point arithmetic  
bme680i.py: Driver using integer arithmentic for the internal calculations according to the BOSCH datasheet. Only for the final result floating point operations are used.  
bmetest.py: Sample test script  
readme.md: This file
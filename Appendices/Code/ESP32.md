---
title: ESP32
---


# boot.py
```import async_mqtt_uart.py```

# esp32_setup.py
```
import os
import time
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()
import upip

# set wifi information
ssid = 'photon'
password = 'particle' 

#create station instance
station = network.WLAN(network.STA_IF)

#set active
station.active(True)

# if the station is not connected,
if not station.isconnected():
    # connect the station with ssid and password
    station.connect(ssid, password)

# wait until the station is connected
while station.isconnected() == False:
  pass

# print connection successful
print('Connection successful')

# print full connection information 
print(station.ifconfig())

#if there is a path named 'lib' in the current directory
if 'lib' in os.listdir('./'):
    # if logging.py is not in the lib directory
    if 'logging.py' not in os.listdir('lib/'):
    	# install the micropython logging library
        upip.install('micropython-logging')

    # if mqtt_async.py is not in the lib directory,
    if 'mqtt_async.py' not in os.listdir('lib/'):
    	# install the micropython mqtt library
        upip.install('micropython-mqtt')
# if there is no 'lib directory', nothing has been downloaded
else:
    # so download both libraries
    upip.install('micropython-logging')
    upip.install('micropython-mqtt')

# once the logging library has been loaded, import it
import logging

# set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# write one debug message
logger.debug(station.ifconfig())
```

# async_mqtt_uart.py

```
# Derived from: 
# * https://github.com/peterhinch/micropython-async/blob/master/v3/as_demos/auart.py
# * https://github.com/tve/mqboard/blob/master/mqtt_async/hello-world.py


from mqtt_async import MQTTClient, config
import uasyncio as asyncio
import time
from machine import UART
import my_oled
import logging
logging.basicConfig(level=logging.DEBUG)

MAXTX = 4

# Change the following configs to suit your environment
TOPIC_PUB = 'EGR314/Team203/mls'
TOPIC_SUB = 'EGR314/Instructor'
config.server = 'egr3x4.ddns.net' # can also be a hostname
config.ssid     = 'photon'
config.wifi_pw  = 'particle'

uart = UART(2, 9600,tx=17,rx=16)
uart.init(9600, bits=8, parity=None, stop=1,flow=0) # init with given parameters

async def receiver():
    b = b''
    sreader = asyncio.StreamReader(uart)
    while True:
        res = await sreader.read(1)
        if res==b'\r':
            await client.publish(TOPIC_PUB, b, qos=1)
            print('published', b)
            b = b''
        else:
            b+=res

def callback(topic, msg, retained, qos):
    print('callback',topic, msg, retained, qos)
    # my_oled.print_data(msg)
    # my_oled.plot_data(msg)
    while (not not msg):
        
        uart.write(msg[:MAXTX])
        time.sleep(.01)
        msg = msg[MAXTX:]

    uart.write('\r\n')
    time.sleep(.01)
  
async def conn_callback(client): await client.subscribe(TOPIC_SUB, 1)

async def main(client):
    await client.connect()
    asyncio.create_task(receiver())
    while True:
        await asyncio.sleep(1)

config.subs_cb = callback
config.connect_coro = conn_callback

client = MQTTClient(config)
loop = asyncio.get_event_loop()
loop.run_until_complete(main(client))
```

# simple_uart_echo

```
# used for ESP 32 testing
# import modules
from machine import UART
from machine import Pin
import time

# initialize a new UART class
uart = UART(2, 9600,tx=17,rx=16)
# run the init method with more details including baudrate and parity
uart.init(9600, bits=8, parity=None, stop=1) 
led = Pin(2,Pin.OUT)

# run forever
while True:
    # read one byte
    c = uart.read(1)
    # if c is not empty:
    if c is not None:
        # write the byte back out to uart
        uart.write(c)
        # print the byte to the shell
        print(c)
        # toggle the onboard LED
        led.value(led.value()^1)
	# sleep for a very small amount of time
        time.sleep(.01)
```

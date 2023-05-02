# async_mqtt_uart.py

```# Derived from: 
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
loop.run_until_complete(main(client))```

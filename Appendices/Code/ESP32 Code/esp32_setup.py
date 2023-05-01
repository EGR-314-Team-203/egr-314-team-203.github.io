#Add your own wifi + password in the ssid and ssid_password spots!
# import libraries
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


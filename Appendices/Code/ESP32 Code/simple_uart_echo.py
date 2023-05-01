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


import ugit
from machine import Pin
import time

pin = Pin(0,Pin.IN,Pin.PULL_UP)
if pin.value() is 0:
    ugit.pull_all()
    
#main code here
TIME_MS=100
LED = Pin("LED", Pin.OUT)
while True:
    LED.off()
    time.sleep_ms(TIME_MS)
    LED.on()
    time.sleep_ms(TIME_MS)

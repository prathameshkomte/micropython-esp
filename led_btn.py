import machine
import time

led = machine.Pin(19,machine.Pin.OUT)
btn = machine.Pin(5,machine.Pin.IN)

while True:
    btn_stat = btn.value()
    if(btn_stat == False):
        led.value(1)
    else:
        led.value(0)
from machine import Pin

led = Pin(2,Pin.OUT)
btn = Pin(0,Pin.IN)

while True:
    btn_stat = btn.value()
    if(btn_stat == False):
        led.value(1)
    else:
        led.value(0)

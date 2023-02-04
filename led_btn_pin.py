from machine import Pin

led = Pin(19,Pin.OUT)
btn = Pin(5,Pin.IN)

while True:
    btn_stat = btn.value()
    if(btn_stat == False):
        led.value(1)
    else:
        led.value(0)

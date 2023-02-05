from machine import ADC, Pin
import time
adc = ADC(Pin(32))
buzzer = Pin(17, Pin.OUT)
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)
ldrval = 0

while True:
    ldrval = adc.read()
    print(ldrval)
    time.sleep(1)
    
    if ldrval >= 2000:
        buzzer.value(0)
    else:
        buzzer.value(1)
    
    




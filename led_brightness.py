from machine import Pin, PWM, ADC
import time

frequency = 12000
led = PWM(Pin(25),frequency)
pot = ADC(Pin(33))
pot.width(ADC.WIDTH_12BIT)
pot.atten(ADC.ATTN_11DB)

while True:
    pot_value = pot.read()
    print(pot_value)
    
    if pot_value < 15:
        led.duty(0)
    else:
        led.duty(pot_value)
        
    time.sleep_ms(5)    
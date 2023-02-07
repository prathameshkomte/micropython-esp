#*****************WiFi AP***********************************
import network

wifi = network.WLAN(network.AP_IF)
wifi.active(True)

wifi.config(essid = 'ISAesp', password = '12345678')

print(wifi.ifconfig())

#********************WiFi station********************************************

#import network

#wifi = network.WLAN(network.STA_IF)
#wifi.active(True)

#wifi.connect('Realme6', '12345678')
#while not wifi.isconnected():
#    pass

#if wifi.isconnected():
#    print(wifi.ifconfig())

#********************WiFi with time limit************************
#import network
#import time

#timeout = 0
#wifi = network.WLAN(network.STA_IF)

#wifi.active(False)
#time.sleep(0.5)
#wifi.active(True)

#wifi.connect('Reelmi', '12345678')

#if not wifi.isconnected():
#    print('connecting...')
#    while(not wifi.isconnected() and timeout < 5):
#        print(5 - timeout)
#        timeout = timeout + 1
#        time.sleep(1)
        
#if(wifi.isconnected()):
#    print("Connected")
#else:
#    print("Time Out")
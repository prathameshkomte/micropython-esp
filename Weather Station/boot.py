# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
try:
  import usocket as socket
except:
  import socket

import network
from machine import Pin
import dht
from time import sleep

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'vivo1952'
password = '96981234'

station = network.WLAN(network.STA_IF)

station.active(True)

while True:
	try:
		station.connect(ssid,password)
	except OSError as e:
		print(e)
	sleep(1)
	if station.isconnected():
		print('Connected') 
		break

print('Connection successful')
print(station.ifconfig())

# sensor = dht.DHT22(Pin(14))
sensor = dht.DHT11(Pin(33))
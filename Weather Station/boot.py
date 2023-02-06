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

ssid = 'your ssid'
password = 'your password'

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

sensor = dht.DHT11(Pin(33))

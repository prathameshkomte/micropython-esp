from machine import ADC, Pin
import time
adc = ADC(Pin(32))
buzzer = Pin(17, Pin.OUT)
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)
ldrval = 0

try:
  import urequests as requests
except:
  import requests
  
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

#Your network credentials
ssid = 'Alfa12'
password = '12345678'

#Your phone number in international format
phone_number = '+919326047375'
#Your callmebot API key
api_key = '2539069'

def connect_wifi(ssid, password):
  #Connect to your network
  station = network.WLAN(network.STA_IF)
  station.active(True)
  station.connect(ssid, password)
  while station.isconnected() == False:
    pass
  print('Connection successful')
  print(station.ifconfig())

def send_message(phone_number, api_key, message):
  #set your host URL
  url = 'https://api.callmebot.com/whatsapp.php?phone='+phone_number+'&text='+message+'&apikey='+api_key

  #make the request
  response = requests.get(url)
  #check if it was successful
  if response.status_code == 200:
    print('Success!')
  else:
    print('Error')
    print(response.text)

# Connect to WiFi
connect_wifi(ssid, password)
# Send message to WhatsApp "Hello"
message = 'Alert%21%20Turn%20ON%20your%20lights' #YOUR MESSAGE HERE (URL ENCODED)https://www.urlencoder.io/ 
#send_message(phone_number, api_key, message) // function for sending alert on whatsapp


while True:
    ldrval = adc.read()
    print(ldrval)
    time.sleep(1)
    
    if ldrval >= 2000:
        buzzer.value(0)      
    else:
        buzzer.value(1)
        send_message(phone_number, api_key, message)








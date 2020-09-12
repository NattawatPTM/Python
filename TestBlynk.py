



import BlynkLib
#import ipstw
import network
import time
import machine

import dht
d = dht.DHT22(machine.Pin(19))

#w=ipstw.IPSTW()
#w.begin()

WIFI_SSID = "Nattawat"
WIFI_PASS = "Nattawat0000"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
#wifi.scan()       
wifi.connect(WIFI_SSID,WIFI_PASS)
while not wifi.isconnected() :
  pass
print(wifi.ifconfig())

BLYNK_AUTH = 'ar6t7d7TNCieS_RnoqIbz_4ubgJ_fJBC'
# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)
# Start Blynk (this call should never return)

def v3_write_handler(value):
  print(value)
 # register the virtual pin
blynk.add_virtual_pin(3, write=v3_write_handler)
def on_connect():
  print("connected")
  
blynk.on_connect(on_connect)
def on_disconnect():
  print("disconnected")
blynk.on_disconnect(on_disconnect)


# Register virtual pin handler
def my_user_task():
  # Read DHT22
  d.measure() 
  t=d.temperature() # eg. 23.6 (閹虹煰) 
  h=d.humidity() # eg. 41.3 (% RH)
  
  #w.fill(0)
  #w.text("Temp=%d " % t,0,0*8)
  #w.text("Humi=%d " % h,0,(1*8)+1)
  #w.show()
  
  print('Temp={}'.format(t))
  print('Humi={}'.format(h))
  
  blynk.virtual_write(1, t)
  blynk.virtual_write(2, h)

# Register task handler
blynk.set_user_task(my_user_task, 2000)

blynk.run()






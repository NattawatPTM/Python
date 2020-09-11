#wifi-ap-udp-server.py
import network
ap_if=network.WLAN(network.AP_IF)
ap_if.active(True)

ap_if.config(essid="EnET-Gr33",password="Nattawat")
ap_if.config(channel=33,authmode=network.AUTH_WPA2_PSK)

import socket
import time
from machine import Pin
port = 4210
LEDr = Pin(5,Pin.OUT)
LEDb = Pin(19,Pin.OUT)
LEDg = Pin(23,Pin.OUT)

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ip=ap_if.ifconfig()[0]
s.bind((ip,port))
print('waiting...')
LEDr.value(1)

while True:
  data,addr=s.recvfrom(1024)
  print('received:',data,'from',addr)
  if(data == b'r'):
    if LEDr.value()==1:
      LEDr.value(1)
      LEDb.value(0)
      LEDg.value(0)
      
    elif LEDr.value()==0:
      LEDg.value(0)
      LEDb.value(1) 
      time.sleep(1.5)
      LEDb.value(0) 
      LEDr.value(1)
      s.sendto("Turn on LEDr\n",addr)
        
  elif(data == b'g'):
    LEDr.value(0)
    LEDb.value(0)
    LEDg.value(1)
    s.sendto("Turn ON LED\n",addr)
  else:
    s.sendto("Unknow command\n",addr)


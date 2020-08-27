#7.2
from machine import Pin
from machine import ADC
from machine import I2C
from ssd1306 import SSD1306_I2C
import NeoPixelLib
import time

sw1=Pin(33,Pin.IN)
sw2=Pin(32,Pin.IN)
adc1=ADC(Pin(34))
adc1.atten(ADC.ATTN_11DB)

i2cbus = I2C(scl=Pin(22), sda=Pin(21) ,freq=400000)
oled = SSD1306_I2C(128,64,i2cbus)

np=NeoPixelLib.NeoPixel(Pin(12),3)


red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yell=(255,255,0)
count1=0
count2=0

def intrsw2(e):
  time.sleep_ms(50)
  if sw2.value()==0:
    global count2
    count2 +=1
    if count2>2:
      count2 = 0
  
sw2.irq(trigger=Pin.IRQ_FALLING,handler=intrsw2)


def intrsw1(e):
  time.sleep_ms(50)
  if sw1.value()==0:
    global count1
    count1 +=1
    if count1>2:
      count1 = 0
  
sw1.irq(trigger=Pin.IRQ_FALLING,handler=intrsw1)
  
while True:
  time.sleep_ms(50)
  value=adc1.read()
  volt=value/4095*3.3
  print("KNOB-SVP =%4d =%0.3f V"%(value,volt))
  oled.fill(0)
  
  

  if count1==0:
    oled.text("RGB 0",35,2)
    if count2==0:
      np[0]=(value//16,0,0)
      oled.text("RED   = %0.3f V"%(volt),0,12)
    elif count2==1:
      np[0]=(0,value//16,0)
      oled.text("GREEN = %0.3f V"%(volt),0,12)
    elif count2==2:
      np[0]=(0,0,value//16)
      oled.text("BLUE  = %0.3f V"%(volt),0,12)
      
  elif count1==1:
    oled.text("RGB 1",35,2)
    if count2==0:
      np[1]=(value//16,0,0)
      oled.text("RED   = %0.3f V"%(volt),0,12)
    elif count2==1:
      np[1]=(0,value//16,0)
      oled.text("GREEN = %0.3f V"%(volt),0,12)
    elif count2==2:
      np[1]=(0,0,value//16)
      oled.text("BLUE  = %0.3f V"%(volt),0,12)
      

  elif count1==2:
    oled.text("RGB 2",35,2)
    if count2==0:
      np[2]=(value//16,0,0)
      oled.text("RED   = %0.3f V"%(volt),0,12)
    elif count2==1:
      np[2]=(0,value//16,0)
      oled.text("GREEN = %0.3f V"%(volt),0,12)
    elif count2==2:
      np[2]=(0,0,value//16)
      oled.text("BLUE  = %0.3f V"%(volt),0,12)
         
  np.write()
  oled.show()





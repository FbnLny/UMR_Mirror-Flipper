
from machine import Pin, Timer
import time, uos


#Define Pins------------------------
dirPin = Pin(15, Pin.OUT, value = 0)
stpPin = Pin(2, Pin.OUT, value = 0)
slpPin = Pin(4, Pin.OUT, value = 1)
rstPin = Pin(16, Pin.OUT, value = 1)
m2Pin = Pin(17, Pin.OUT, value = 0)
m1Pin = Pin(5, Pin.OUT, value = 1)
m0Pin = Pin(18, Pin.OUT, value = 0)
enaPin = Pin(19, Pin.OUT, value = 0)

print("Starting: quarter-step-mode, driver enabled")

def setMicroSteps(uSteps):
  if uSteps == 32:
    m0Pin.value(1)
    m1Pin.value(0)
    m2Pin.value(1)
  elif uSteps == 16:
    m0Pin.value(0)
    m1Pin.value(0)
    m2Pin.value(1)
  elif uSteps == 8:
    m0Pin.value(1)
    m1Pin.value(1)
    m2Pin.value(0)
  elif uSteps == 4:
    m0Pin.value(0)
    m1Pin.value(1)
    m2Pin.value(0)
  elif uSteps == 2:
    m0Pin.value(1)
    m1Pin.value(0)
    m2Pin.value(0)
  elif uSteps == 1:
    m0Pin.value(0)
    m1Pin.value(0)
    m2Pin.value(0)
  else:
    print("Error: # of µ-steps not supported: using halfstep-mode")
    m0Pin.value(1)
    m1Pin.value(0)
    m2Pin.value(0)

def moveStep(dir):
  if dir == 0 or dir == 1:
    dirPin.value(dir)
    time.sleep_us(100)
    stpPin.value(1)
    time.sleep_us(200)
    stpPin.value(0)
    #print("Moved")
  else:
    print("Error: incorrect direction value, use 0 or 1")

def driverSlp():
  slpPin.value(0)
      
def driverWake():
  slpPin.value(1)
  time.sleep_ms(3)
  
def flipMirror(self):
  global direction
  for i in range(200):
    moveStep(direction)
    time.sleep_ms(10)
  if direction == 0:
    direction = 1
  else:
    direction = 0
	
def getFreq():
  f = open("freq.txt", "r")
  return int(f.read())
	
direction = 0
freq = getFreq() * 1000



tim0 = Timer(0)
tim0.init(period=freq, mode=Timer.PERIODIC, callback=flipMirror)

#try:
#  while True:
#    pass
#except KeyboardInterrupt:
#  tim0.deinit()




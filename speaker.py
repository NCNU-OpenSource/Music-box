# Speaker
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

from led import *

GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 50)
p.stop()

freq = [523,587,659,698,784,880,988]
tone = ["Do","Re","Mi","Fa","So","La","Si"]

inst = [0,0,0,0,0,0,0]
def play(n):
  for i in range(6):
      inst[6-i] = inst[5-i]
  inst[0] = n

  p.start(25)
  p.ChangeFrequency(freq[n-1])
  for j in range(2000):
    for i in range(7):
        init()
        glow(inst[i],i+1)
  p.ChangeFrequency(1)
  p.stop()
  time.sleep(0.04)

def init2():
  for i in range(7):
      inst[i] = 0

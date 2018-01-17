# 8*8 LED Matrix
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

row = [2,22,18,17,25,23,9]
column = [10,4,24,3,8,7,27]

for i in row:
    GPIO.setup(i,GPIO.OUT)
for i in column:
    GPIO.setup(i,GPIO.OUT)

def init():
    for i in row:
        GPIO.output(i,0)
    for i in column:
        GPIO.output(i,1)

def glow(n,m):
    for i in range(n):
        GPIO.output(row[i],1);
    GPIO.output(column[m-1],0);

import RPi.GPIO as GPIO
import time
from keypad import *
from speaker import *
from led import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

bee = [5,3,3, 4,2,2, 1,2,3,4,5,5,5, 5,3,3, 4,2,2, 1,3,5,5,1]
tiger = [1,2,3,1, 1,2,3,1, 3,4,5, 3,4,5, 5,6,5,4,3,1, 5,6,5,4,3,1]
bridge = [5,6,5,4,3,4,5, 2,3,4, 3,4,5, 5,6,5,4,3,4,5, 2,5,3,1]
diff = [6,5,6, 6,5,5,3,5,5,6,2,5,3,3, 3,2,1,2,3, 2,1,2,5,3]
song = []

pre = 2000
record = 0      #recording mode
while 1:
  key = get_key()
  tmp = key
  if (tmp == pre):
     continue
  pre = key
  if (key == 1000):
     continue
  elif (key == 'A'):
     print("Playing the 'We Are Different'.")
     for i in range(len(diff)):
         play(diff[i])
     init()
     init2()
  elif (key == 'B'):
     print("Playing the 'Tiger'")
     for i in range(len(tiger)):
         play(tiger[i])
     init()
     init2()
  elif (key == 'C'):
     print("Playing the 'London Bridge is falling down'")
     for i in range(len(bridge)):
         play(bridge[i])
     init()
     init2()
  elif (key == 'D'):
     print("Playing the 'Bee'")
     for i in range(len(bee)):
         play(bee[i])
     init()
     init2()
  elif (key == '*'):
     record = 1
     print("Recording...")
  elif (key == '#'):
     record = 0
     print("Playing the song record.")
     for i in range(len(song)):
         play(song[i])
     init()
     init2()
  elif (key == '0'):
     del song[:]
     print("Your song had already eliminate.")
  else:
     init()
     glow(ord(key)-48,1)
     p.start(25)
     print(tone[ord(key)-49])
     p.ChangeFrequency(freq[ord(key)-49])
     for i in range(14000):
         glow(ord(key)-48,1)
     p.ChangeFrequency(1)
     p.stop()
     if (record):
        song.append(ord(key)-48)

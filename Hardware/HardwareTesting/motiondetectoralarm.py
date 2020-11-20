
import RPi.GPIO as GPIO
import time

sensor = 4
buzzer = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.output(buzzer,False)
from time import sleep
print("Initialzing PIR Sensor......")
time.sleep(12)
print("PIR Ready...")


try: 
   while True:
      if GPIO.input(sensor):
          GPIO.output(buzzer,GPIO.HIGH)
          sleep(2)
          GPIO.output(buzzer,GPIO.LOW)
          
          print("Motion Detected")
          while GPIO.input(sensor):
              time.sleep(0.2)
      else:
          GPIO.output(buzzer,GPIO.LOW)


except KeyboardInterrupt:
    GPIO.cleanup()

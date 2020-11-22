import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(40, GPIO.IN)
GPIO.setup(38, GPIO.OUT)
GPIO.output(38, GPIO.LOW)
while True:
   #val=input("1 for on, 0 for off: ")
   val2=GPIO.input(40)
   if val2==GPIO.HIGH:
       GPIO.output(7, GPIO.HIGH)
       GPIO.output(38, GPIO.HIGH)
       time.sleep(10)
       GPIO.output(38, GPIO.LOW)
   else:
       GPIO.output(7, GPIO.LOW)
   print(val2)
   time.sleep(1)
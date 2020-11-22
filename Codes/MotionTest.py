import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.OUT)
while True:
    if GPIO.input(7)==1:
        print ("Motion")
        GPIO.output(11, 0)
        time.sleep(0.1)
    elif GPIO.input(7)==0:
            print("No Motion")
            GPIO.output(11, 1)
            time.sleep(0.1)
       
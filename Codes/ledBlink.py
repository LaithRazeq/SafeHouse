import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
while True:

    GPIO.output(11,0)
    time.sleep(1) 
    GPIO.output(11, 1)
    time.sleep(1)

import RPi.GPIO as GPIO
import time

channel = 7

def configLock():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(7, GPIO.LOW)
    
def lock(lockIsOn):
    if lockIsOn:
        GPIO.output(7, GPIO.HIGH)
    else:
        GPIO.output(7, GPIO.LOW)
    
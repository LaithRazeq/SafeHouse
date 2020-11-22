import RPi.GPIO as GPIO
import time

channel = 38

def configBuzzer():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(channel, GPIO.LOW)
    
def buzz(buzzerIsOn):
    if buzzerIsOn:
        GPIO.output(channel, GPIO.HIGH)
        time.sleep(10)
        GPIO.output(channel, GPIO.LOW)    
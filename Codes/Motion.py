import RPi.GPIO as GPIO
import time

channel = 40

def configMotion():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.IN)

def motionDetect(motionIsOn)-> int:
    if motionIsOn and GPIO.input(channel).HIGH:
        return 1
    return 0
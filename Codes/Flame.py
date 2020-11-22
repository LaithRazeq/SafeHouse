import RPi.GPIO as GPIO
import timeq

channel = 36


def configureFlame():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.IN)


def flameDetect(flameIsOn) -> int:
    if flameIsOn and GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=300): #GPIO could be high
        return 1
    return 0

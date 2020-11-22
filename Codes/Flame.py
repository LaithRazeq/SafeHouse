import RPi.GPIO as GPIO
import time

channel = 36
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN)
def configFlame():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.IN)


def flameDetect(flameIsOn) -> int:
    if flameIsOn==1: #GPIO could be high
            if GPIO.input(channel)==0:          
                return 1
            else:
                return 0
    else:
        return 0

'''   
while True:
    flameDetect(1)
    time.sleep(0.1)
    


#GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=300)
           #I=GPIO.add_event_callback(channel, callback)


'''
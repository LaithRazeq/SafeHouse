"""
This file runs the configurations and main functionality of the flame sensor. 

Author(s):  Azizul Hasan
Co-Author(s): Ahmed Abdelrazik, Laith Abdelrazeq 
Last Modified: 8-DEC-2020
"""
import RPi.GPIO as GPIO
import time

#Channel that flame sensor is connected to
channel = 36

def configFlame()->int:
    '''
    Returns 1 if successful, this funtion configures the flame sensor on the RPI. 
    '''    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.IN)
    return 1


def flameDetect(flameIsOn:int) -> int:
    '''
    Checks param flameIsOn if 1 then check the input from the channel and return
    the current status of the sensor. If flameIsOn is 0 returns 2; used for 
    testing purposes. Any another input is invalid returns 0. 
    '''
    if flameIsOn==1: 
            if GPIO.input(channel)==0:          
                return 1
            else:
                return 0
    elif flameIsOn==0:
        return 2
    else:
        return 0

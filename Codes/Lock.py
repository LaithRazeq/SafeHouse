"""
This file runs the configurations and main functionality of the relay which is 
connected to the lock. 

Author(s):  Laith Abdelrazeq
Co-Author(s): Ahmed Abdelrazik  
Last Modified: 8-DEC-2020
"""
import RPi.GPIO as GPIO
import time

#Channel that relay is connected to
channel = 7

def configLock()->int:
    '''
    Returns 1 if successful, this funtion configures the relay on the RPI. 
    '''    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(7, GPIO.LOW)
    return 1
    
def lock(lockIsOn:int)->int:
    '''
    Returns 1 if input is valid 0 otherwise, this function checks the param 
    buzzerIsOn if 1 activates lock.
    '''    
    if lockIsOn==1:
        GPIO.output(7, GPIO.HIGH)
        return 1
    elif lockIsOn==0:
        GPIO.output(7, GPIO.LOW)
        return 1
    else:
        return 0
    
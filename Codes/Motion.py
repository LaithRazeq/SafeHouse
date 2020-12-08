"""
This file runs the configurations and main functionality of the flame sensor. 

Author(s): Ramit Mahajan
Co-Author(s): Ahmed Abdelrazik, Laith Abdelrazeq 
Last Modified: 8-DEC-2020
"""
import RPi.GPIO as GPIO
import time

#Channel that motion sensor is connected to
channel = 40

def configMotion()->int:
    '''
    Returns 1 if successful, this funtion configures the motion sensor on the RPI. 
    '''    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.IN)
    return 1

def motionDetect(motionIsOn:int)-> int:
    '''
    Checks param motionIsOn if 1 then check the input from the channel and return
    the current status of the sensor. If motionIsOn is 0 returns 2; used for 
    testing purposes. Any another input is invalid return 0. 
    '''    
    if motionIsOn==1:
        if GPIO.input(channel)==1:
            return 1
        else:
            return 0
    elif motionIsOn==0:
        return 2
    else:
        return 0
"""
This file runs the configurations and main functionality of the Buzzer. 

Author(s):  Ramit Mahajan
Co-Author(s): Ahmed Abdelrazik, Laith Abdelrazeq 
Last Modified: 8-DEC-2020
"""
import RPi.GPIO as GPIO
import time

#Channel that buzzer is connected to
channel = 38 

def configBuzzer()->int:
    '''
    Returns 1 if successful, this funtion configures the buzzer on the RPI. 
    '''
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(channel, GPIO.LOW)
    return 1
    
def buzz(buzzerIsOn:int)->int:
    '''
    Returns 1 if input is valid 0 otherwise, this function checks the param 
    buzzerIsOn if 1 activates buzzer for 5 seconds.
    '''
    if buzzerIsOn==1:
        GPIO.output(channel, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(channel, GPIO.LOW)
        return 1
    elif buzzerIsOn==0:
        return 1
    else:
        return 0

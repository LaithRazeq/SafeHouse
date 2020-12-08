"""
This file runs the Controller and all its functionalities, to start run the 
script and enter 1 to start or 0 to exit. This file needs to run on a RPI.

Author(s): Laith Abdelrazeq
Co-Author(s): Ahmed Abdelrazik, Azizul Hassan
Last Modified: 8-DEC-2020
"""
from TSCommand import thingspeak_read_c
from Buzzer import*
from Lock import*
from Motion import*
from Flame import*
import datetime
import time
import picamera

##ThingSpeak Channels' Information 

ID = "1160874" # TS Command ID
READ_KEY="YOLQ8V4RT6JCZE8Q" # TS Command Read Key
WRITE_KEY="IOOAC36UJI0C2JFI" # TS History Write Key

##Global Variables

isArmed=0
motionIsOn=0
flameIsOn=0
lockIsOn=0
cameraIsOn=0
buzzerIsOn=0

#Reading current date & time
gino= datetime.datetime.now()
D=(str(gino.year)+'-'+str(gino.month)+'-'+str(gino.day))
T=(str(gino.hour)+':'+str(gino.minute)+':'+str(gino.second))

##Functions

def getTime():
    '''
    This function updates global variables D & T, which represent current 
    date and time.
    '''
    global gino
    global D
    global T
    gino= datetime.datetime.now()
    D=(str(gino.year)+'-'+str(gino.month)+'-'+str(gino.day))
    T=(str(gino.hour)+':'+str(gino.minute)+':'+str(gino.second))
    

#Main function running the system
def main():
    configSystem()
    while True:
        getTime()
        updateStatus()
        lock(lockIsOn)
        if isArmed == 1:
            print(lock(lockIsOn))
            if motionDetect(motionIsOn) == 1:
                takeAction(0) 
            if flameDetect(flameIsOn) == 1:
                takeAction(1)
        time.sleep(1)

#Configuring the System
def configSystem()->int:
    '''
    Returns 1 if successful. this function configures the system by callin all 
    the config functions from their respective files.
    '''
    configMotion()
    configFlame()
    configLock()
    configBuzzer()
    return 1

#Updating the sensor's status from the thingSpeak command channel       
def updateStatus()->int:
    '''
    Returns 1 if successful, this function updates the global variables from the 
    TS Command Channel, these variables will then be checked to know which 
    hardware is activated by the client.
    '''
    global isArmed
    global lockIsOn
    global cameraIsOn
    global buzzerIsOn
    global motionIsOn
    global flameIsOn
    curr_status=thingspeak_read_c(READ_KEY,ID)
    isArmed=int(curr_status[0])
    lockIsOn=int(curr_status[1])
    cameraIsOn=int(curr_status[2])
    buzzerIsOn=int(curr_status[3])
    motionIsOn=int(curr_status[4])
    flameIsOn=int(curr_status[5])
    return 1

#Take action function        
def takeAction(sensor: int)->int:
    '''
    Returns 1 if entry valid 0 otherwise, this function will take an action upon
    the value of the param sensor, the function will take an action and write to 
    the TS History channel by calling updateHistory function.
    '''
    if sensor==0:
#         print("Motion Detected!!")
        recordVideo(cameraIsOn)
        buzz(buzzerIsOn)
        updateHistory(0, cameraIsOn)
        return 1
    elif sensor==1:
#         print("Fire Detected!!")
        buzz(buzzerIsOn)
        recordVideo(cameraIsOn)
        updateHistory(1, cameraIsOn)
        return 1
    else:
        return 0

#Updating the history thingspeak upon the occurence of an event    
def updateHistory(sensor:int,cameraIsOn:int)->int:
    '''
    Returns 1 if entry valid 0 otherwise, this function will write to the 
    TS Histroy channel based on which snesor is active ,param sensor, and also 
    upon whether the camera is active or not, param camerIsOn. 
    '''
    if sensor==0 and cameraIsOn==0:   
        sen="Motion"
        thingspeak_write_h(ID, D, T, sen, "NA", WRITE_KEY)
        return 1
    elif sensor==1 and cameraIsOn==0:
        sen="Flame"
        thingspeak_write_h(ID, D, T, sen, "NA", WRITE_KEY)
        return 1
    elif sensor==0 and cameraIsOn==1:
        sen="Motion"
        thingspeak_write_h(ID, D, T, sen, '/home/pi/Desktop/security', WRITE_KEY)
        return 1
    elif sensor==1 and cameraIsOn==1:
        sen="Flame"
        thingspeak_write_h(ID, D, T, sen, '/home/pi/Desktop/security', WRITE_KEY)
        return 1
    else:
        return 0
        
def recordVideo(cameraIsOn:int)->int:
    '''
    Return 1 if entry valid 0 otherwise, this function configures and the 
    records a video if param cameraIsOn is 1, and saves this vedio in the 
    specified location and with the current date and time of the incident.
    '''
    if cameraIsOn==1:
        with picamera.PiCamera() as camera:
            camera.resolution=(1280, 720)
            camera.rotation = (180)
            camera.start_preview(alpha=192)
            camera.start_recording('/home/pi/Desktop/security/{}.h264'.format(gino))
            time.sleep(5)
            camera.stop_preview()
            camera.stop_recording()
        return 1
    elif cameraIsOn==0:
        return 1
    else:
        return 0

## Main Script
    
x = int(input("To start system press 1/ Press 0 to quit: "))
if x==1:
    main()
else:
    print("bye")

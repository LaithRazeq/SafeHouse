from TSHistory import thingspeak_write
from TSCommand import read_data_thingspeak
from Camera import*
from Buzzer import*
from Lock import*
from Motion import*
from Flame import*
import datetime
import time

##ThingSpeak Channels' Information 
ID = "1160874" # TS Command ID
READ_KEY="YOLQ8V4RT6JCZE8Q" # TS Command Read Key
WRITE_KEY="IOOAC36UJI0C2JFI" # TS History Write Key
##Date and Time
gino= datetime.datetime.now()
D=(str(gino.year)+'-'+str(gino.month)+'-'+str(gino.day))
T=(str(gino.hour)+':'+str(gino.minute)+':'+str(gino.second))
##Global Variables
isArmed=False
motionIsOn=False
flameIsOn=False
lockIsOn=False
cameraIsOn=False
buzzerIsOn=False

##Main function running the system
def main():
    configSystem()
    while True:
        updateStatus()
        if isArmed:
            lock(lockIsOn)
            if motionDetect(motionIsOn):
                takeAction(0) 
            if flameDetect(flameIsOn):
                takeAction(1)
        time.sleep(1)

##Configuring the System
def configSystem():
    configMotion()
    configFlame()
    configLock()
    configCamera()
    configBuzzer()

##Updating the sensor's status from the thingSpeak command channel       
def updateStatus():
    curr_status=read_data_thingspeak(READ_KEY,ID)
    isArmed=curr_status[0]
    lockIsOn=curr_status[1]
    cameraIsOn=curr_status[2]
    buzzerIsOn=curr_status[3]
    motionIsOn=curr_status[4]
    flameIsOn=curr_status[5]
    #time.sleep(1)

##Take action function        
def takeAction(sensor):
    if sensor==0:
        print("Motion Detected!!")
        buzz(buzzerIsOn)
        recordVideo(cameraIsOn)
        updateHistory(0)
    else:
        print("Fire Detected!!")
        buzz(buzzerIsOn)
        recordVideo(cameraIsOn)   
        updateHistory(1)

##Updating the history thingspeak upon the occurence of an event    
def updateHistory(sensor):
    if sensor==0:   
        sen="Motion"
    if sensor==1:
        sen="Flame"
    if cameraIsOn:
        thingspeak_write(ID, D, T, sen, "C:/Desktop/video", 1, WRITE_KEY)
    else:
        thingspeak_write(ID, D, T, sen, "NA", 1, WRITE_KEY)

##Run the main
main()
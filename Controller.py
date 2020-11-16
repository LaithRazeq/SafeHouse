from TSHistory import thingspeak_write
from TSCommand import read_data_thingspeak
import datetime
import time



gino= datetime.datetime.now()
date=(str(gino.year)+'-'+str(gino.month)+'-'+str(gino.day))
t=(str(gino.hour)+':'+str(gino.minute)+':'+str(gino.second))

ID = 2

READ_KEY="M8JC1XL6I75J08KL"
WRITE_KEY="Y10RFX27NP5XFP5L"


def updateStatus():
    curr_status=read_data_thingspeak(READ_KEY)
    ARM=curr_status[0]
    LOCK=curr_status[1]
    CAM=curr_status[2]
    BUZZ=curr_status[3]
    MOTION=curr_status[4]
    
    print("System Status:\nArmed:"+ARM+", Door Locked:"+LOCK+", Camera:"+CAM+", Buzzer:"+BUZZ+", MOTION:"+MOTION)
    
    
def updateHistory():
    x=10
    while x>0:
        mot="motion"+str(x)
        thingspeak_write(ID, date, t, mot, "C:/Desktop", 1, WRITE_KEY)
        x-=1
        time.sleep(1)


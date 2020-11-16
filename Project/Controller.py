from TSHistory import thingspeak_write
from TSCommand import read_data_thingspeak
import datetime
import time



gino= datetime.datetime.now()
date=(str(gino.year)+'-'+str(gino.month)+'-'+str(gino.day))
t=(str(gino.hour)+':'+str(gino.minute)+':'+str(gino.second))

ID = "1160874" # TS Command ID

READ_KEY="YOLQ8V4RT6JCZE8Q" # TS Command Read Key
WRITE_KEY="Y10RFX27NP5XFP5L" # TS Command Write Key
ARM=0
LOCK=0
CAM=0
BUZZ=0
MOTION=0


def updateStatus()->str:
    curr_status=read_data_thingspeak(READ_KEY,ID)
    ARM=curr_status[0]
    LOCK=curr_status[1]
    CAM=curr_status[2]
    BUZZ=curr_status[3]
    MOTION=curr_status[4]
    
    status = ("System Status:\nArmed:"+ARM+", Door Locked:"+LOCK+", Camera:"+CAM+", Buzzer:"+BUZZ+", MOTION:"+MOTION+"\n")
    return status
    
    
def updateHistory():
    x=10
    while x>0:
        mot="motion"+str(x)
        thingspeak_write(ID, date, t, mot, "C:/Desktop", 1, WRITE_KEY)
        x-=1
        time.sleep(1)


##Test function
def test(desc:str, expected:str, actual:str)->str:
    print(desc)
    print("\nExpected result:\n", expected, "\nActual result:\n", actual)
    if expected == actual:
        print("Test passed")     
    else:
        print("Test failed") 

##Main Script
test('Testing updateStatus()','System Status:\nArmed:1, Door Locked:0, Camera:0, Buzzer:0, MOTION:0\n',updateStatus())
updateHistory()
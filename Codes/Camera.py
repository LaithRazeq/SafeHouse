import picamera
from time import sleep
import datetime

'''
Setting up date/time retreaval
'''
gino= datetime.datetime.now()
date=(str(gino.year)+'-'+str(gino.month)+'-'+str(gino.day))
t=(str(gino.hour)+':'+str(gino.minute)+':'+str(gino.second))

def configCamera():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        
    
def recordVideo(camerIsOn):
    if(cameraIsOn):
        camera.start_recording('/home/pi/Desktop/motion.h264')
        camera.wait_recording(10)
        camera.stop_recording()        
        
    
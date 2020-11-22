import picamera
from time import sleep


with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.rotation = (180)
    camera.start_preview(alpha=192)
    #camera.start_recording('/home/pi/Desktop/my_video.h264')
    sleep(20)
    camera.stop_preview()
  

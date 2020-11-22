import picamera
from time import sleep
import keyboard
    

  

while True:
    with picamera.PiCamera() as camera:
        camera.resolution = (1280,720)
        camera.start_preview(alpha=192)
        #camera.start_recording('/home/pi/Desktop/my_video.h264')
        
        #camera.stop_preview()

        #sleep(20)
        if keyboard.is_pressed('esc'):
            camera.stop_preview()
            break


  

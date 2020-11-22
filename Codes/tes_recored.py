import picamera
from time import sleep


with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview(alpha=192)
    sleep(3)
    camera.start_recording('/home/pi/Desktop/motion.h264')
    camera.wait_recording(10)
    camera.stop_preview()
    camera.stop_recording()

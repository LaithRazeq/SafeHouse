import RPi.GPIO as GPIO
import time
import picamera


with picamera.PiCamera() as camera:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(40, GPIO.IN)
    GPIO.setup(38, GPIO.OUT)
#PIO.output(7, GPIO.LOW)
    GPIO.output(38, GPIO.LOW)
    camera.resolution = (640, 480)
    camera.rotation = (180)
    
    while True:
   #val=input("1 for on, 0 for off: ")
       val2=GPIO.input(40)
       if val2==GPIO.HIGH:
           GPIO.output(7, GPIO.HIGH)
           GPIO.output(38, GPIO.HIGH)
           camera.start_preview(alpha=192)
           #sleep(3)
           camera.start_recording('/home/pi/Desktop/motion.h264')
           camera.wait_recording(7)
           #time.sleep(10)
           camera.stop_preview()
           camera.stop_recording()
           GPIO.output(38, GPIO.LOW)
           GPIO.output(7, GPIO.LOW)
           break
       else:
           GPIO.output(7, GPIO.LOW)
      


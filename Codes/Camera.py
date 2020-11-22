# import picamera
# from time import sleep
# import datetime
# 
# '''
# Setting up date/time retreaval
# '''
# gino= datetime.datetime.now()
# date=(str(gino.year)+'-'+str(gino.month)+'-'+str(gino.day))
# t=(str(gino.hour)+':'+str(gino.minute)+':'+str(gino.second))


# import picamera
# from time import sleep
# 
# 
# with picamera.PiCamera() as camera:
#     camera.resolution = (640, 480)
#     camera.start_preview(alpha=192)
#     sleep(3)
#     camera.start_recording('/home/pi/Desktop/motion.h264')
#     camera.wait_recording(10)
#     camera.stop_preview()
#     camera.stop_recording()
# 
# def configCamera():
#     print('camera')
#     
#         
#     
# def recordVideo(cameraIsOn):
#     if(cameraIsOn):
#         camera.start_recording('/home/pi/Desktop/'+str(gino)+'.h264')
#         camera.wait_recording(10)
#         camera.stop_recording()        
#         
    
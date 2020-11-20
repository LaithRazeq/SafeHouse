from gpiozero import MotionSensor

pir = MotionSensor(4)
while True :
    pir.wait_for_motion()
    print("Motion is detected")
    pir.wait_for_no_motion()
    print("Motion is Stopped")
    

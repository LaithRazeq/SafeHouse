from gpiozero import MotionSensor
from signal import pause

motionsensor = MotionSensor(4)
while True :
    print(input("1 for ON and 0 for OFF :"))
    if input==1:
        MotionSensor.on
    if input==0:
        MotionSensor.off

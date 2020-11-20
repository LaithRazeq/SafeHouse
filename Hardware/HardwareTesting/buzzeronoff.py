from gpiozero import Buzzer


buzzer= Buzzer(4)
while True :
    print(input("1 for ON and 0 for OFF :"))
    if input==1:
        buzzer.on
    if input==0:
        buzzer.off

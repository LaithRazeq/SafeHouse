import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

Buzzer = 17

def setup(pin):
        global BuzzerPin
        BuzzerPin = pin
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(BuzzerPin, GPIO.OUT)
        GPIO.output(BuzzerPin, GPIO.HIGH)

def on():
        GPIO.output(BuzzerPin, GPIO.HIGH)

def off():
        GPIO.output(BuzzerPin, GPIO.LOW)

def beep(x):
        on()
        time.sleep(x)
        off()

def loop():
        while True:
                beep(0.03)
                time.sleep(0.05)
                beep(0.03)
                time.sleep(1)

def destroy():
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.cleanup() # Release resource

if __name__ == '__main__': # Program start from here
    setup(Buzzer)
    try:
        loop()
    except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
        destroy()

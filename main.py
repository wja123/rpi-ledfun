import RPi.GPIO as GPIO
from time import sleep
from threading import Timer

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! You may need superuser privileges")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

mode = GPIO.getmode()
pinArr = [4, 18, 17, 27, 22]

GPIO.setup(4, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

def ledOn(pin):
    GPIO.output(pin, True)


#GPIO.output(4, True)
#GPIO.output(18, True)
#GPIO.output(17, True)
#GPIO.output(27, True)
#GPIO.output(22, True)


GPIO.output(4, False)
GPIO.output(18, False)
GPIO.output(17, False)
GPIO.output(27, False)
GPIO.output(22, False)






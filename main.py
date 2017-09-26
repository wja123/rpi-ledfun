import RPi.GPIO as GPIO

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! You may need superuser privileges")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

mode = GPIO.getmode()
GPIO.setup(4, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# GPIO.output(4, True)
# GPIO.output(18, True)
# GPIO.output(17, True)
# GPIO.output(27, True)
# GPIO.output(22, True)


GPIO.output(4, False)
GPIO.output(18, False)
GPIO.output(17, False)
GPIO.output(27, False)
GPIO.output(22, False)






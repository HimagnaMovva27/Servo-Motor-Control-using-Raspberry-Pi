import RPi.GPIO as GPIO
import time

servo_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

p = GPIO.PWM(servo_pin, 50)  # 50Hz for servo
p.start(2.5)

try:
    while True:
        p.ChangeDutyCycle(5)   # Move servo
        time.sleep(0.5)
        p.ChangeDutyCycle(7.5) # Another position
        time.sleep(0.5)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
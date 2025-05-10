import RPi.GPIO as GPIO
import time

buzzer_pin = 38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzer_pin, GPIO.OUT, initial=GPIO.LOW)  # 默认低电平，蜂鸣器静音

def beep(duration=2,volume=50):

    if volume>100:
        volume=100

    if volume<20:
        volume=20

    buzzer_pwm = GPIO.PWM(buzzer_pin, 100)
    buzzer_pwm.start(volume)

    #print("BUZZER ON")

    time.sleep(duration)
    GPIO.output(buzzer_pin, GPIO.LOW)   # 低电平静音


#beep()
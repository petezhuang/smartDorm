import RPi.GPIO as GPIO
import time

led=16

led_status=False
led_mode="AUTO"
led_intense=5

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(led, GPIO.OUT)
pwm_led=GPIO.PWM(led,100)
pwm_led.start(0)

def get_led_mode():
    return led_mode

def get_led_intensity():
    return led_intense

def led_on():
    global led_status
    global led_intense

    led_status=True

    #print("led on")

    pwm_led.start(20+led_intense*8)

def led_off():
    global led_status

    led_status=False

    #print("led off")
    pwm_led.stop()

def change_led_mode(mode):
    global led_mode
    led_mode=mode

def change_intense(intense):
    global led_intense

    if intense < 0:
        intense = 0

    if intense > 10:
        intense = 10

    led_intense=intense
# led_on(50)
# time.sleep(2)
# led_off()
# led_on(100)
# time.sleep(2)
# led_off()
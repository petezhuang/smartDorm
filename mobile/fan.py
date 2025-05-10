import RPi.GPIO as GPIO
import time

#设置 GPIO 模式为 BOARD
GPIO.setmode(GPIO.BOARD)

#定义引脚
STBY = 35
PWMA = 29
AIN1 = 31
AIN2 = 33

fan_mode="AUTO"

#初始化GPIO
GPIO.setup(STBY, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)

#定义软件PWM
pwma = GPIO.PWM(PWMA,300)

speed=50

#改变风扇转速，建议转速20-80
#树莓派供电不够，不建议在后续代码中随意更改参数
def change_speed(sp):
    global speed
    speed=sp

#打开风扇
def fan_on():
    GPIO.output(STBY, GPIO.HIGH)
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    pwma.start(speed)
    #time.sleep(20)
    #fan_off()

#关闭风扇
def fan_off():
    GPIO.output(STBY, GPIO.LOW)
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)

def get_fan_mode():
    return fan_mode

def change_fan_mode(mode):
    global fan_mode
    fan_mode=mode

#fan_on()
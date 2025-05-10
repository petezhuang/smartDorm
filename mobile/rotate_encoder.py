import RPi.GPIO as GPIO
import time

# 引脚定义
BUTTON_PIN = 26  # C相/按钮
CLK_PIN = 24  # A相/CLK
DT_PIN = 22  # B相/DT

# 全局变量
counter = 0
clk_last_state = 0
button_last_state = True
debounce_time = 0.15  # 防抖时间(秒)

# 初始化GPIO
GPIO.setmode(GPIO.BOARD)  # 使用BCM编号
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(CLK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 读取初始状态
clk_last_state = GPIO.input(CLK_PIN)
button_last_state = GPIO.input(BUTTON_PIN)


def rotary_change(clk_state, dt_state):
    # global counter

    if clk_state != dt_state:
        # counter += 1
        # print("正转 | 计数器:", counter)

        return 2#2代表正转

    else:
        # counter -= 1
        # print("反转 | 计数器:", counter)

        return 3#3代表反转

def rotary_detect():
    global button_last_state
    global clk_last_state

    # print("旋转编码器测试开始...")
    # print("旋转旋钮或按下按钮进行测试")

    while True:
        # 检测按钮按下（带防抖）
        button_state = GPIO.input(BUTTON_PIN)

        if button_state != button_last_state:
            time.sleep(debounce_time)

            if GPIO.input(BUTTON_PIN) == GPIO.LOW:
                return 1#1代表按钮按下

                #print("按钮按下!")

            button_last_state = button_state

        # 检测旋转（带状态变化确认）
        clk_state = GPIO.input(CLK_PIN)

        if clk_state != clk_last_state:
            dt_state = GPIO.input(DT_PIN)

            # 确认状态变化有效
            if GPIO.input(CLK_PIN) == clk_state:  # 再次读取确认
                return rotary_change(clk_state, dt_state)
            clk_last_state = clk_state

        time.sleep(0.001)  # 更短的延迟提高响应速度

#print(rotary_detect())
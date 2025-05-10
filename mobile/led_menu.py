import time
from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from time import sleep

import led_light
import rotate_encoder

# 初始化端口
serial = i2c(port=1, address=0x3C)
# 初始化设备
device = ssd1306(serial)
device.clear()

led_key_num = 0

select_line_led = 1

def change_intense():
    tmp_key=0

    while True:
        if tmp_key==2:
            if led_light.led_intense!=10:
                led_light.led_intense+=1

        if tmp_key==3:
            if led_light.led_intense!=0:
                led_light.led_intense-=1

        with canvas(device) as draw:
            draw.text((2, 0), "<-BACK", fill="white")
            draw.text((2, 16), "Led Intense: " + str(led_light.led_intense), fill="white")
            draw.text((2, 32), "Led Mode: " + str(led_light.led_mode), fill="white")

            # 被选中的行（反色高亮）
            draw.rectangle((6*13, 16, 2+6*13+6*2, 32), fill="white")  # 背景填充白色
            draw.text((2, 16), "Led Intense: ", fill="white")
            draw.text((2+6*13,16),str(led_light.led_intense), fill="black")# 文字黑色
            if tmp_key==1:
                return

        tmp_key=rotate_encoder.rotary_detect()

def change_mode():
    tmp_key = 0

    while True:
        if tmp_key == 2:
            if led_light.led_mode=="AUTO":
                led_light.led_mode="ON"

            elif led_light.led_mode=="ON":
                led_light.led_mode="OFF"

            elif led_light.led_mode=="OFF":
                led_light.led_mode="AUTO"

        if tmp_key == 3:
            if led_light.led_mode=="AUTO":
                led_light.led_mode="OFF"

            elif led_light.led_mode=="OFF":
                led_light.led_mode="ON"

            elif led_light.led_mode=="ON":
                led_light.led_mode="AUTO"

        with canvas(device) as draw:
            draw.text((2, 0), "<-BACK", fill="white")
            draw.text((2, 16), "Led Intense: " + str(led_light.led_intense), fill="white")
            draw.text((2, 32), "Led Mode: " + str(led_light.led_mode), fill="white")

            # 被选中的行（反色高亮）
            draw.rectangle((6 * 10, 32, 2 + 6 * 14 + 6, 48), fill="white")  # 背景填充白色
            draw.text((2, 16), "Led Intense: ", fill="white")
            draw.text((2 + 6 * 10, 32), str(led_light.led_mode), fill="black")  # 文字黑色
            if tmp_key == 1:
                return

        tmp_key = rotate_encoder.rotary_detect()

def led_menu(key_num):
    global select_line_led

    if key_num == 2:
        if select_line_led != 3:
            select_line_led += 1

    if key_num == 3:
        if select_line_led != 1:
            select_line_led -= 1

    with canvas(device) as draw:
        if select_line_led == 1:
            draw.text((2, 0), "<-BACK", fill="white")
            draw.text((2, 16), "Led Intense: " + str(led_light.led_intense), fill="white")
            draw.text((2, 32), "Led Mode: " + str(led_light.led_mode), fill="white")

            # 被选中的行（反色高亮）
            draw.rectangle((0, 0, device.width, 16), fill="white")  # 背景填充白色
            draw.text((2, 0), "<-BACK", fill="black")  # 文字黑色
            if key_num == 1:
                return -1

        if select_line_led == 2:
            draw.text((2, 0), "<-BACK", fill="white")
            draw.text((2, 16), "Led Intense: " + str(led_light.led_intense), fill="white")
            draw.text((2, 32), "Led Mode: " + str(led_light.led_mode), fill="white")

            # 被选中的行（反色高亮）
            draw.rectangle((0, 16, device.width, 32), fill="white")  # 背景填充白色
            draw.text((2, 16), "Led Intense: " + str(led_light.led_intense), fill="black")  # 文字黑色

            if key_num == 1:
                return 1

        if select_line_led == 3:
            draw.text((2, 0), "<-BACK", fill="white")
            draw.text((2, 16), "Led Intense: " + str(led_light.led_intense), fill="white")
            draw.text((2, 32), "Led Mode: " + str(led_light.led_mode), fill="white")

            # 被选中的行（反色高亮）
            draw.rectangle((0, 32, device.width, 48), fill="white")  # 背景填充白色
            draw.text((2, 32), "Led Mode: " + str(led_light.led_mode), fill="black")  # 文字黑色

            if key_num == 1:
                return 2

def led_menu_control():
    time.sleep(0.1)

    global led_key_num
    global select_line_led

    select_line_led = 1
    led_key_num = 0

    while True:
        menu=led_menu(led_key_num)

        if menu==-1 :
            return

        #跳转到亮度调整菜单
        if menu == 1:
            change_intense()
            led_key_num = 0
            continue

        #跳转到模式转换菜单
        if menu == 2:
            change_mode()
            led_key_num = 0
            continue

        led_key_num = rotate_encoder.rotary_detect()
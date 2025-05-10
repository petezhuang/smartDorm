import time
import threading

from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106

import fan
import rotate_encoder

# 初始化端口
serial = i2c(port=1, address=0x3C)
# 初始化设备
device = ssd1306(serial)
device.clear()

fan_key_num = 0

select_line_fan = 1

def change_mode():
    tmp_key=0

    while True:
        if tmp_key == 2:
            if fan.fan_mode=="AUTO":
                fan.fan_mode="ON"

            elif fan.fan_mode=="ON":
                fan.fan_mode="OFF"

            elif fan.fan_mode=="OFF":
                fan.fan_mode="AUTO"

        if tmp_key == 3:
            if fan.fan_mode=="AUTO":
                fan.fan_mode="OFF"

            elif fan.fan_mode=="OFF":
                fan.fan_mode="ON"

            elif fan.fan_mode=="ON":
                fan.fan_mode="AUTO"

        with canvas(device) as draw:
            draw.text((2, 0), "<-BACK", fill="white")
            draw.text((2, 16), "Fan Mode: ", fill="white")

            # 被选中的行（反色高亮）
            draw.rectangle((6*10 , 16, 2+6*14+6, 32), fill="white")  # 背景填充白色
            draw.text((2+6*10, 16), str(fan.fan_mode), fill="black")  # 文字黑色

            if tmp_key == 1:
                return

        tmp_key = rotate_encoder.rotary_detect()

def fan_menu(key_num):
    global select_line_fan

    if key_num == 2:
        if select_line_fan != 2:
            select_line_fan += 1

    if key_num == 3:
        if select_line_fan != 1:
            select_line_fan -= 1

    with canvas(device) as draw:
        if select_line_fan == 1:
            draw.text((2, 0), "<-BACK", fill="white")
            draw.text((2, 16), "Fan Mode: " + str(fan.fan_mode), fill="white")

            # 被选中的行（反色高亮）
            draw.rectangle((0, 0, device.width, 16), fill="white")  # 背景填充白色
            draw.text((2, 0), "<-BACK", fill="black")  # 文字黑色

            if key_num == 1:
                return -1

        if select_line_fan == 2:
            draw.text((2, 0), "<-BACK", fill="white")
            draw.text((2, 16), "Fan Mode: " + str(fan.fan_mode), fill="white")

            # 被选中的行（反色高亮）
            draw.rectangle((0, 16, device.width, 32), fill="white")  # 背景填充白色
            draw.text((2, 16), "Fan Mode: " + str(fan.fan_mode), fill="black")  # 文字黑色

            if key_num == 1:
                return 1

def fan_menu_control():
    time.sleep(0.1)

    global fan_key_num
    global select_line_fan

    select_line_fan = 1
    fan_key_num = 0

    while True:
        menu=fan_menu(fan_key_num)

        if menu == -1:
            return

        if menu == 1:
            change_mode()
            fan_key_num=0
            continue

        fan_key_num = rotate_encoder.rotary_detect()
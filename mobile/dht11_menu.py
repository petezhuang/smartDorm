import time
import threading

from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106

import rotate_encoder

import dht11_controller

# 初始化端口
serial = i2c(port=1, address=0x3C)
# 初始化设备
device = ssd1306(serial)
device.clear()

dht11_key_num = 0

select_line_dht11 = 1

def dht11_menu(key_num):
    global select_line_dht11

    with canvas(device) as draw:
        if select_line_dht11 == 1:
            draw.text((2, 0), "<-BACK", fill="white")
            draw.text((2, 16), "Tmp: "+str(dht11_controller.tmp) , fill="white")
            draw.text((2, 32),"Hum: "+str(dht11_controller.hum) , fill="white")

            # 被选中的行（反色高亮）
            draw.rectangle((0, 0, device.width, 16), fill="white")  # 背景填充白色
            draw.text((2, 0), "<-BACK", fill="black")  # 文字黑色

            if key_num == 1:
                return -1

def dht11_menu_control():
    time.sleep(0.1)

    global dht11_key_num
    global select_line_dht11

    select_line_dht11 = 1
    dht11_key_num = 0

    while True:
        menu=dht11_menu(dht11_key_num)

        if menu==-1:
            return

        dht11_key_num = rotate_encoder.rotary_detect()
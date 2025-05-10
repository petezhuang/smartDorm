import time
import threading

from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106

import fan
import fan_menu
import fan_controller

import rotate_encoder

import led_light
import led_menu
import led_controller

import dht11_controller
import dht11_menu

import gas_controller
import gas_menu

import build_json

# 初始化端口
serial = i2c(port=1, address=0x3C)
# 初始化设备
device = ssd1306(serial)
device.clear()

select_line=1
key_num=0

#多线程实时监控参数
#LED状态检测线程
thread1=threading.Thread(target=led_controller.monitor_led_mode)
#LED亮度检测线程
thread2=threading.Thread(target=led_controller.monitor_led_intense)
#FAN状态检测线程
thread3=threading.Thread(target=fan_controller.monitor_fan_mode)
#温湿度检测线程
thread4=threading.Thread(target=dht11_controller.monitor_tmp_hum)
#气体浓度检测线程
thread5=threading.Thread(target=gas_controller.monitor_co2_co)
#人物检测线程
thread6=threading.Thread(target=led_controller.monitor_human)
#json构建线程
thread7=threading.Thread(target=build_json.build)

#创建守护线程
thread1.daemon=True
thread2.daemon=True
thread3.daemon=True
thread4.daemon=True
thread5.daemon=True
thread6.daemon=True
thread7.daemon=True

def menu1(key_num):
    global select_line

    if key_num == 1:
        return select_line

    if key_num == 2:
        if select_line != 4:
            select_line += 1

    if key_num == 3:
        if select_line != 1:
            select_line -= 1

    with canvas(device) as draw:
        if select_line == 1:
            draw.text((2, 0), "Led status", fill="white")
            draw.text((2, 16), "Fan status", fill="white")
            draw.text((2, 32), "Temp & Hum", fill="white")
            draw.text((2, 48), "Gas", fill="white")

            # 被选中的行（反色高亮）
            draw.rectangle((0, 0, device.width, 16), fill="white")  # 背景填充白色
            draw.text((2, 0), "Led status", fill="black")  # 文字黑色

        if select_line == 2:
            draw.text((2, 0), "Led status", fill="white")
            draw.text((2, 16), "Fan status", fill="white")
            draw.text((2, 32), "Temp & Hum", fill="white")
            draw.text((2, 48), "Gas", fill="white")

            # 被选中的行（反色高亮）
            draw.rectangle((0, 16, device.width, 32), fill="white")  # 背景填充白色
            draw.text((2, 16), "Fan status", fill="black")  # 文字黑色

        if select_line == 3:
            draw.text((2, 0), "Led status", fill="white")
            draw.text((2, 16), "Fan status", fill="white")
            draw.text((2, 32), "Temp & Hum", fill="white")
            draw.text((2, 48), "Gas", fill="white")

            # 被选中的行（反色高亮）
            draw.rectangle((0, 32, device.width, 48), fill="white")  # 背景填充白色
            draw.text((2, 32), "Temp & Hum", fill="black")  # 文字黑色

        if select_line == 4:
            draw.text((2, 0), "Led status", fill="white")
            draw.text((2, 16), "Fan status", fill="white")
            draw.text((2, 32), "Temp & Hum", fill="white")
            draw.text((2, 48), "Gas", fill="white")

            # 被选中的行（反色高亮）
            draw.rectangle((0, 48, device.width, 64), fill="white")  # 背景填充白色
            draw.text((2, 48), "Gas", fill="black")  # 文字黑色

    return 0

#开启多线程
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()

while True:
    menu=menu1(key_num)
    #print(menu)

    if menu == 1:
        led_menu.led_menu_control()
        key_num = 0
        continue

    if menu == 2:
        fan_menu.fan_menu_control()
        key_num = 0
        continue

    if menu == 3:
        dht11_menu.dht11_menu_control()
        key_num = 0
        continue

    if menu == 4:
        gas_menu.gas_menu_control()
        key_num = 0
        continue

    key_num = rotate_encoder.rotary_detect()
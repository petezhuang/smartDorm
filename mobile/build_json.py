from dht11_controller import get_tmp,get_hum
from led_light import get_led_mode,get_led_intensity
from led_controller import get_sit_time
from fan import get_fan_mode
import json
import time
from datetime import datetime
import post_json
import get_json

def build():
    while True:
        get_json.get_json()

        data = {
            "temperature": str(get_tmp()),  # 从 dht11_controller 导入的温度
            "humidity": str(get_hum()),  # 从 dht11_controller 导入的湿度
            "led_mode": get_led_mode(),  # 从 led_light 导入的LED模式
            "led_intensity": str(get_led_intensity()),  # 从 led_light 导入的LED强度
            "sit_time": str(get_sit_time()),  # 从 led_controller 导入的坐的时间
            "fan_mode": get_fan_mode(),  # 从 fan 导入的风扇模式
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 当前时间
        }

        # 将数据写入 data.json 文件
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)  # indent=4 用于美化输出，便于阅读

        post_json.post_json()

        time.sleep(1)
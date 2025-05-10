import requests
import json
from fan import change_fan_mode
from led_light import change_led_mode,change_intense
import time
data={}
def get_json():
    try:
        global data
        url='https://www.u2601175.nyat.app:15108/api/echo'
        headers = {'Content-Type': 'application/json'}
        response=requests.get(url, headers=headers, verify=False)
        tmp_data=data
        data = response.json()

        change_fan_mode(data['fan'])
        change_led_mode(data['lamp'])
        change_intense(int(data['led_intensity']))

    except Exception as e:
        pass
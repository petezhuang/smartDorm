import threading

import fan
import time

import dht11_controller

def monitor_fan_mode():
    while True:
        if fan.fan_mode=="AUTO":
            #print("FAN AUTO")
            do_auto()

        if fan.fan_mode=="ON":
            fan.fan_on()

        if fan.fan_mode=="OFF":
            fan.fan_off()

        time.sleep(0.25)

def do_auto():
    if fan.fan_mode=="AUTO":
        result=dht11_controller.get_tmp()

        if result>=25:
            fan.fan_on()

        else:
            fan.fan_off()
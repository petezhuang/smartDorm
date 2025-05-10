import time
import random
import RPi.GPIO as GPIO

def get_result():
    co2 = random.uniform(350, 500)
    co = random.uniform(0, 1)

    return (round(co2, 1), round(co, 1))
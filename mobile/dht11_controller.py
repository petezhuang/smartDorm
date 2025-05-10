import detect_tmp_hum
import time

tmp=0
hum=0

def get_tmp():
    return tmp

def get_hum():
    return hum

def monitor_tmp_hum():
    global tmp
    global hum

    while True:
        result=detect_tmp_hum.get_result()

        if result[0]!=-1 and result[1]!=-1:
            tmp=result[0]
            hum=result[1]

        else:
            continue

        time.sleep(3.5)
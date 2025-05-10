import gas
import time

co=0
co2=0

def monitor_co2_co():
    global co
    global co2

    while True:

        result = gas.get_result()

        if result[0] != -1 and result[1] != -1:
            co2 = result[0]
            co = result[1]

        else:
            continue

        time.sleep(3.5)

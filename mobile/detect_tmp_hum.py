import RPi.GPIO as GPIO
import time
import random

def get_result():
    bit = []
    dura_time = []

    K = 0  # 定义循环初始值

    GPIO.setmode(GPIO.BOARD)  # 定义GPIO编码方式
    time.sleep(2)
    Pin = 12  # 定义引脚，使用哪个就定义哪个
    GPIO.setup(Pin, GPIO.OUT)
    GPIO.output(Pin, 0)  # 向dht11发送低电平（开始信号）

    time.sleep(0.02)
    GPIO.output(Pin, 1)
    GPIO.setup(Pin, GPIO.IN)

    while GPIO.input(Pin) == 0:  # 采用轮训检测dht的响应信号，如果输入高电平将跳出此循环
        continue

    while GPIO.input(Pin) == 1:  # 采用轮训检测dht的响应信号
        continue

    while K < 40:  # 循环40次用以接收dht11的40bit数据

        while GPIO.input(Pin) == 0:
            continue

        begin = time.time()  # 低电平循环结束故此时是高电平信号，因此开始计时

        while GPIO.input(Pin) == 1:  # 轮训高电平
            continue

        end = time.time()  # 获取高电平信号的结束时间

        # dura_time.append(end-begin)#此处为了确定0和1的高电平持续时间

        if (end - begin) < 0.000035:  # 检测高电平的持续时间判断输入是0还是1（0.00003可以自测一下，取一个适合你的时间）
            bit.append(0)  # 高电平小于0.000035s证明是0

        else:
            bit.append(1)  # 高电平大于0.000035s证明是1
        K = K + 1  # 记录循环次数

    # print(Time)				#观察时间特点

    humidity1bit = bit[0:8]  # 根据dht11的信号原理获取所需的值
    humidity2bit = bit[8:16]
    temperature1bit = bit[16:24]
    temperature2bit = bit[24:32]
    checks_bits = bit[32:40]
    humidity1 = 0
    humidity2 = 0
    temperature1 = 0
    temperature2 = 0
    check = 0

    for i in range(0, 8):

        humidity1 += humidity1bit[i] * (2 ** (7 - i))
        humidity2 += humidity2bit[i] * (2 ** (7 - i))
        temperature1 += temperature1bit[i] * (2 ** (7 - i))
        temperature2 += temperature2bit[i] * (2 ** (7 - i))
        check += checks_bits[i] * (2 ** (7 - i))

    temperature = temperature1 + temperature2 * 0.1  # 获取温度值
    humidity = humidity1 + humidity2 * 0.1
    check_num = temperature1 + humidity1 + temperature2 + humidity2  # 计算前32位数的值

    if check_num == check:  # 检查前32位的值是否与校验位相等
        return (temperature, humidity)
        #print("temp:%s,hum:%s" % (temperature, humidity))  # 相等输出温度和湿度

    else:
        return (-1,-1)
        #print("dht11 check was wrong.  checknum:%s check:%s" % (check_num, check))  # 不等输出前32位值和校验位值

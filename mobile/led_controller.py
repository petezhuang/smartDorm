import threading

import buzzer

import led_light
import time

import cv2
from picamera2 import Picamera2

# 加载 Haar Cascade 人脸检测模型（OpenCV 自带）
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 初始化 Picamera2
picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (640, 480)})
picam2.configure(config)
picam2.start()
no_detected=0
detected=0
sit_time=0

def monitor_led_mode():
    while True:
        # if led_light.led_mode=="AUTO":
        #     print("AUTO")

        if led_light.led_mode=="OFF":
            led_light.led_off()

        if led_light.led_mode=="ON":
            led_light.led_on()

        time.sleep(0.25)

def monitor_led_intense():
    while True:
        led_light.change_intense(led_light.led_intense)

        time.sleep(0.25)

def monitor_human():
    global no_detected
    global detected
    global face_cascade
    global picam2
    global sit_time

    while True:
        # 捕获图像
        img=cv2.imread("./DZ.jpg")
        #frame = picam2.capture_array()
        frame=img.copy()

        # 转换为灰度图（人脸检测需要）
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 检测人脸
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

        # 在图像上标记人脸
        # for (x, y, w, h) in faces:
        #     cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        #
        # # 显示图像（可选）
        # cv2.imshow("Camera Feed", frame)
        # if cv2.waitKey(1) == ord('q'):  # 按 'q' 退出
        #     break

        # 如果检测到人脸，保存照片
        detected += 1

        sit_time += 3

        if len(faces) > 0:
            no_detected=0

            if led_light.led_mode=="AUTO":
                led_light.led_on()

            print(f"检测到{len(faces)}个人脸")
        else:
            no_detected=no_detected+1

            #30秒未检测到有人则关灯
            if no_detected>=10:
                if led_light.led_mode=="AUTO":
                    led_light.led_off()

            #20分钟未检测到人脸，重置久坐时间
            if no_detected>=400:
                sit_time=0
                detected=0
            print("未检测到人脸")

        if detected>=2400:
            buzzer.beep(duration=3)#久坐报警3秒
            detected=0#清空检测记录，防止持续报警
        # 等待 3 秒
        time.sleep(3)

def get_sit_time():
    return sit_time
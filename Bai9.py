import numpy as np
import cv2
import RPi.GPIO as GPIO
from config import Config
from MJPEG import mjpeg
import time



GPIO.setmode(GPIO.BCM)
GPIO.setup(Config.BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Config.BT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Config.BT3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Config.BT4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# global capture
namewindown = "Camera men :v"
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
capture.set(cv2.CAP_PROP_SATURATION,0.2)
print("capture is ok")
cap_img = True

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
cap_video = False
cap_stream = False

print("preprape video")
while(capture.isOpened()):
    ret, frame = capture.read()
    
    
    # cv2.imshow('Video frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    if GPIO.input(Config.BT1) == 0 and cap_img==True:
        cv2.imshow(namewindown , frame)
        cap_img = False
        continue
    if GPIO.input(Config.BT2) == 0:
        cv2.imshow(namewindown, frame)
        out.write(frame)
        continue
    print(cap_video)
    if cap_video == True:
        print("OK True")
        cv2.imshow(namewindown, frame)
        out.write(frame)
        
    if GPIO.input(Config.BT3) == 0:
        print("press BT3")
        
        if cap_video == True:
            cap_video = False
            cv2.destroyWindow(namewindown)
            
            continue
        
        print("CAP_FALSE")
        if cap_video == False:
            print("OK")
            cap_video = True
            continue
        time.sleep(0.5)
    if GPIO.input(Config.BT4) == 0:
        if cap_video == False:
            print("OK")
            cap_video = True
            continue
    
    # cv2.destroyWindow(namewindown)
    cap_img = True


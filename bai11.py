
import cv2
import numpy as np
import copy
import RPi.GPIO as GPIO
from config import Config
def nothing(x):
    pass


# Open the camera
cap = cv2.VideoCapture(0) 
 
# Create a window
# cv2.namedWindow('image')
 
# # create trackbars for color change
# cv2.createTrackbar('lowH','image',0,180,nothing)
# cv2.createTrackbar('highH','image',179,180,nothing)
 
# cv2.createTrackbar('lowS','image',0,255,nothing)
# cv2.createTrackbar('highS','image',255,255,nothing)
 
# cv2.createTrackbar('lowV','image',0,255,nothing)
# cv2.createTrackbar('highV','image',255,255,nothing)

GPIO.setmode(GPIO.BCM)
GPIO.setup(Config.BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Config.BT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def draw(contours, frame):
    for i in range(len(contours)):
        hull = cv2.convexHull(contours[i])
        cv2.drawContours(frame, [hull], -1, (0,255,0))





def main():
    isdraw = False 
    while(True):
        ret, src = cap.read()
        frame = copy.copy(src)
    
        # get current positions of the trackbars
        # ilowH = cv2.getTrackbarPos('lowH', 'image')
        # ihighH = cv2.getTrackbarPos('highH', 'image')
        # ilowS = cv2.getTrackbarPos('lowS', 'image')
        # ihighS = cv2.getTrackbarPos('highS', 'image')
        # ilowV = cv2.getTrackbarPos('lowV', 'image')
        # ihighV = cv2.getTrackbarPos('highV', 'image')
    
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_hsv = np.array([72, 89, 87])
        higher_hsv = np.array([85, 245, 221])
        # Apply the cv2.inrange method to create a mask
        # mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
        mask = cv2.inRange(hsv, (lower_hsv), higher_hsv)

        _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if GPIO.input(Config.BT2) == GPIO.LOW:
            isdraw = True

        if isdraw == True:
            draw(contours, frame)

        # Apply the mask on the image to extract the original color
        result = cv2.bitwise_or(frame, frame, mask=mask)

        cv2.imshow("Camera", src)
        cv2.imshow('Threshold', result)

        # Press q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
print("isPreprape")
while True:
    
    if GPIO.input(Config.BT1) == 0:
        main()
        break 
 
cap.release()
cv2.destroyAllWindows()
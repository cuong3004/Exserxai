
import cv2
import numpy as np
import copy
import RPi.GPIO as GPIO
from config import Config
def nothing(x):
    pass


# Open the camera
cap = cv2.VideoCapture(0) 
print("Cap ok")
 
# Create a window
cv2.namedWindow('image')
 
# create trackbars for color change
cv2.createTrackbar('lowH','image',0,180,nothing)
cv2.createTrackbar('highH','image',179,180,nothing)
 
cv2.createTrackbar('lowS','image',0,255,nothing)
cv2.createTrackbar('highS','image',255,255,nothing)
 
cv2.createTrackbar('lowV','image',0,255,nothing)
cv2.createTrackbar('highV','image',255,255,nothing)

GPIO.setmode(GPIO.BCM)
GPIO.setup(Config.BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
    
    while(True):



        # src = cv2.imread('image.jpg')
        _, src = cap.read()

        # get current positions of the trackbars
        ilowH = cv2.getTrackbarPos('lowH', 'image')
        ihighH = cv2.getTrackbarPos('highH', 'image')
        ilowS = cv2.getTrackbarPos('lowS', 'image')
        ihighS = cv2.getTrackbarPos('highS', 'image')
        ilowV = cv2.getTrackbarPos('lowV', 'image')
        ihighV = cv2.getTrackbarPos('highV', 'image')

        hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
        lower_hsv = np.array([ilowH, ilowS, ilowV])
        higher_hsv = np.array([ihighH, ihighS, ihighV])
        # Apply the cv2.inrange method to create a mask
        # mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
        mask = cv2.inRange(hsv, (lower_hsv), higher_hsv)

        # Apply the mask on the image to extract the original color
        result = cv2.bitwise_or(src, src, mask=mask)

        cv2.imshow('image', result)

        # Press q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

while True:
    if GPIO.input(Config.BT1) == 0:
        main()
        break 

cap.release()
cv2.destroyAllWindows()
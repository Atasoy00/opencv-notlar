import cv2
import numpy as np

cap = cv2.VideoCapture("video.mp4")
while 1:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    sensivity = 15
    lower_white = np.array([0,0,255-sensivity])
    upper_white = np.array([255,sensivity,255])
    mask = cv2.inRange(hsv,lower_white,upper_white)
    result = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    #cv2.imshow("mask",mask)
    cv2.imshow("result",result)

    k = cv2.waitKey(10) & 0xFF
    if k ==27:
        break
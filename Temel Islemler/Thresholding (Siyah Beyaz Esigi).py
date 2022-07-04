import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",(500,500))

cv2.createTrackbar("Lower-H","Trackbar",0,180,nothing)
cv2.createTrackbar("Lower-S","Trackbar",0,255,nothing)
cv2.createTrackbar("Lower-V","Trackbar",0,255,nothing)

cv2.createTrackbar("Upper-H","Trackbar",0,180,nothing)
cv2.createTrackbar("Upper-S","Trackbar",0,255,nothing)
cv2.createTrackbar("Upper-V","Trackbar",0,255,nothing)

cv2.setTrackbarPos("Upper-H","Trackbar",180)
cv2.setTrackbarPos("Upper-S","Trackbar",255)
cv2.setTrackbarPos("Upper-V","Trackbar",255)

img = cv2.imread("camaro.jpg")

frame1 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

while True:

    lower_h = cv2.getTrackbarPos("Lower-H","Trackbar")
    lower_s = cv2.getTrackbarPos("Lower-S","Trackbar")
    lower_v = cv2.getTrackbarPos("Lower-V", "Trackbar")

    upper_h = cv2.getTrackbarPos("Upper-H","Trackbar")
    upper_s = cv2.getTrackbarPos("Upper-S", "Trackbar")
    upper_v = cv2.getTrackbarPos("Upper-V", "Trackbar")

    lower_color = np.array([lower_h,lower_s,lower_v])
    upper_color = np.array([upper_h,upper_s,upper_v])

    mask = cv2.inRange(frame1,lower_color,upper_color)

    cv2.imshow("Orijinal Goruntu",img)
    cv2.imshow("Maskelenmis Goruntu",mask)
    cv2.waitKey(0)

cv2.destroyAllWindows()

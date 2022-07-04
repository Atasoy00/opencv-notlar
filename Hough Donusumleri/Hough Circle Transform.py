import cv2
import numpy as np

img1 = cv2.imread("coins.jpg")

img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(img,5)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,img.shape[0]/4,param1=200,param2=10,minRadius=10,maxRadius=70)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img1,(i[0],i[1]),i[2],(0,255,0),2)

cv2.imshow("Resim",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


while ()
    düz git
    anormal durum kontrolü (sağ)
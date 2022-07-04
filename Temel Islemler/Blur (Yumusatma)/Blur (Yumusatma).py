import cv2
import numpy as np

img = cv2.imread("OpenCV_Logo.png")


img1 = cv2.blur(img,(5,5))
img2 = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
img3 = cv2.medianBlur(img,5)
img4 = cv2.bilateralFilter(img,9,75,75)


cv2.imshow("1",img)
cv2.imshow("2",img1)
cv2.imshow("3",img2)
cv2.imshow("4",img3)
cv2.imshow("5",img4)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

img = cv2.imread("camaro.jpg")

kernel = np.ones((10,10),np.uint8)

erosion = cv2.erode(img,kernel,iterations=1) #inceltir
dilation = cv2.dilate(img,kernel,iterations=1) #kalınlaştırır
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)


cv2.imshow("Pencere",img)
#cv2.imshow("Pencere1",erosion)
#cv2.imshow("Pencere2",dilation)
#cv2.imshow("Pencere3",opening)
#cv2.imshow("Pencere4",closing)
#cv2.imshow("Pencere5",gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()
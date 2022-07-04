import cv2
import numpy as np


img = cv2.imread("yazi.jpg")

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img1 = np.float32(img1)

koseler = cv2.goodFeaturesToTrack(img1,100,0.01,10)


koseler = np.int0(koseler)

for corner in koseler:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,(0,0,255),-1)

cv2.imshow("Pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

img = cv2.imread("contour.png")
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)

contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contours,1,(0,0,255),3) #-1,0,1 

cv2.imshow("contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
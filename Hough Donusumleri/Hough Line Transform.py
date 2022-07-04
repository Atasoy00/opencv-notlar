import cv2
import numpy as np

img = cv2.imread("hline.png")
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(imgray,75,150)

lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=200)
print(lines[:])


for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow("Pencere1",img)
cv2.imshow("Pencere2",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

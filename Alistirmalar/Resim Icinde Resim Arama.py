import cv2
import numpy as np

img0 = cv2.imread("starwars.jpg")
img = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)

template0 = cv2.imread("starwars2.jpg")
template = cv2.cvtColor(template0,cv2.COLOR_BGR2GRAY)


w,h = template.shape[::-1] #-1, x ve y nin yerini değiştirir

result = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
location = np.where(result > 0.95) #renk değeri 0.95 ten büyük olanları al


for point in zip(*location[::-1]): #-1, x ve y nin yerini değiştirir
    cv2.rectangle(img0,point,(point[0]+w,point[1]+h),(255,255,255),3)


cv2.imshow("Image",img0)
cv2.waitKey(0)
cv2.destroyAllWindows()


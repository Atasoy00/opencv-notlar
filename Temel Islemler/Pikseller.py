import cv2
import numpy as np

img = cv2.imread("camaro.jpg")

renkler = img[150,200]
dimensions = img.shape
print("150,200 Pixelinin Renkleri:",renkler)
print("Resim Boyutları",dimensions)

a = img[20,30,0] #20. satır 30.sütundaki pikselin mavi değerini [(bgr)(012)] a değişkenine atar
print(a)

img[20,30,0] = 150
print(img[20,30,0])

img.itemset((20,30,0),250)
print(img[20,30,0])



cv2.imshow("Cerceve",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
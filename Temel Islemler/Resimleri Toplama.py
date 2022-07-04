import cv2
import numpy as np

Resim1 = np.zeros((512,512,3),np.uint8) +255
cv2.circle(Resim1, (256,256), 150, (0,255,0), -1)

Resim2 = np.zeros((512,512,3),np.uint8) +255
cv2.rectangle(Resim2, (120,120), (375,375), (0,0,255), -1)

Toplam = cv2.add(Resim1, Resim2) #matris olarak beyaz + renk = beyaz

cv2.imshow("Resim1",Resim1)
cv2.imshow("Resim2",Resim2)
cv2.imshow("Toplam",Toplam)

cv2.waitKey(0)
cv2.destroyAllWindows()

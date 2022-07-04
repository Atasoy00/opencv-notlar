import cv2
import numpy as np

Resim1 = np.zeros((512,512,3),np.uint8) +255
cv2.circle(Resim1, (256,256), 150, (0,255,0), -1)

Resim2 = np.zeros((512,512,3),np.uint8) +255
cv2.rectangle(Resim2, (120,120), (375,375), (0,0,255), -1)

dst = cv2.addWeighted(Resim1,0.3,Resim2,0.4,100)




cv2.imshow("Resim1",Resim1)
cv2.imshow("Resim2",Resim2)
cv2.imshow("Toplam",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

img = np.zeros((1,6,3),dtype=np.uint8)

img[0,0] = (255,0,0)
img[0,1] = (200,0,0)
img[0,2] = (150,0,0)
img[0,3] = (100,0,0)
img[0,4] = (50,0,0)
img[0,5] = (0,0,0)

img = cv2.resize(img, (640,480), interpolation = cv2.INTER_AREA)

cv2.imshow("Canvas",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
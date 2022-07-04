import cv2
import numpy as np

tuval = np.zeros((512,512,3), dtype=np.uint8) #+255

cv2.line(tuval, (0,0), (512,512), (0,255,0), thickness=50)
cv2.line(tuval, (512,0), (0,512), (0,255,0), thickness=50)
cv2.line(tuval, (256,0), (256,512), (0,255,0), thickness=50)
cv2.line(tuval, (0,256), (512,256), (0,255,0), thickness=50)
cv2.circle(tuval, (256,256), 250, (0,0,0), thickness=250)

cv2.imshow("Tuval",tuval)
cv2.waitKey(0)
cv2.destroyAllWindows()
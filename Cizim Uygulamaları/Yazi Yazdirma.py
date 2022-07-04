import cv2
import numpy as np


tuval = np.zeros((512,512,3), dtype=np.uint8)

cv2.putText(tuval,"1 2 3 4 5", (5,256), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), cv2.LINE_AA)

cv2.imshow("Tuval",tuval)
cv2.waitKey(0)
cv2.destroyAllWindows()
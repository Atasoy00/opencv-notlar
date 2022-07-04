import cv2

img = cv2.imread ( 'bad_hist_foto.png' , 0)
equ = cv2.equalizeHist (img)

cv2.imshow("Pencere1", img)
cv2.imshow("Pencere2", equ)
cv2.waitKey(0)
cv2.destroyAllWindows()
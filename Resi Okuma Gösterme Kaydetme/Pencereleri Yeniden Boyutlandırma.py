import cv2

img0 = cv2.imread("camaro.jpg")

img1 = cv2.resize(img0,(740,480))


cv2.imshow("Pencere",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
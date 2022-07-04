import cv2

img = cv2.imread("camaro.jpg") #klasik BGR okur

rgb_Resim = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
hsv_Resim = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
gray_Resim = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Resim1",img)
cv2.imshow("Resim2",rgb_Resim)
cv2.imshow("Resim3",hsv_Resim)
cv2.imshow("Resim4",gray_Resim)


cv2.waitKey(0)
cv2.destroyAllWindows()
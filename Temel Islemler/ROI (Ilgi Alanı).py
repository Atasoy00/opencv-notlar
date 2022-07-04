import cv2

img = cv2.imread("camaro.jpg")

print(img.shape[:2])

roi = img[105:300, 60:400]

cv2.imshow("Resim",img)
cv2.imshow("Kesit",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
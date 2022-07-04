import cv2

img1 = cv2.imread("1.png")
img2 = cv2.imread("2.png")

img3 = cv2.bitwise_and(img1,img2)
img4 = cv2.bitwise_or(img1,img2)
img5 = cv2.bitwise_xor(img1,img2)
img6 = cv2.bitwise_not(img1)
img7 = cv2.bitwise_not(img2)

while True:
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    cv2.imshow("1", img1)
    cv2.imshow("2", img2)
    cv2.imshow("3", img7)

cv2.destroyAllWindows()
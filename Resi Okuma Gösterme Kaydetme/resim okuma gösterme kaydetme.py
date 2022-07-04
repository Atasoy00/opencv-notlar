import cv2
import numpy
import matplotlib

img0 = cv2.imread("camaro.jpg") #resmi alma "'dan sonra 0 yazarsan siyah beyaz alır

# print(img0) #resmi matrisli gösterme


cv2.namedWindow("Pencere",cv2.WINDOW_NORMAL) #resmi boyutlandırılabilir yapma

cv2.imshow("Pencere",img0) #resmi gösterme
cv2.imwrite("camaro1.jpg",img1) #resmi camaro1.jpg ismiyle kaydetme

cv2.waitKey(0) #resmi kapayana kadar tutma
cv2.destroyAllWindows() #tüm pencereleri kapama
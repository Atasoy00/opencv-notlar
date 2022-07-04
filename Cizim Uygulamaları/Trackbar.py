import cv2
import numpy as np

def nothing(x): #crateTrackbar komutunu kullanabilmek için boş bir fonk oluşturduk
    pass

tuval = np.zeros((512,512,3),np.uint8)
cv2.namedWindow("Resim") #crateTrackbar komutunu kullanabilmek için pencere ismi belirledik

cv2.createTrackbar("Red","Resim",0,255,nothing)    #kırmızı için 0-255 arası değer alan trackbar oluşturduk
cv2.createTrackbar("Green","Resim",0,255,nothing)
cv2.createTrackbar("Blue","Resim",0,255,nothing)


cv2.createTrackbar("Switch","Resim",0,1,nothing) #0 veya 1 değeri alan switch oluşturuldu

while True: #sürekli denetim için sonsuz döngü
    cv2.imshow("Resim",tuval)
    if cv2.waitKey(1) & 0xFF == ord('q'): #q tuşu ile kapama
        break

    r = cv2.getTrackbarPos("Red","Resim") #kırmızı trackbarın ne konumda olduğunu öğren
    g = cv2.getTrackbarPos("Green","Resim")
    b = cv2.getTrackbarPos("Blue","Resim")

    s = cv2.getTrackbarPos("Switch","Resim") #switch in ne konumda olduğunu öğren

    if s == 0:  #switch 0 ise siyah göster değil ise renkleri göster
        tuval[:] = [0,0,0]
    else:
        tuval[:] = [b,g,r]

cv2.destroyAllWindows()
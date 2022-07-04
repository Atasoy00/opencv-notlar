import cv2


cap = cv2.VideoCapture(0) #video yakalama

while True: #sonsuz döngü
    ret,frame = cap.read()     #ret framein doğru okunmasına göre True/False alır
                               # frame okunan frame kaydedilir
    frame = cv2.flip(frame, 1) #resmi ters çevirir

    cv2.imshow("Webcam", frame)
    cv2.waitKey(30)  #frame geçiş hızı / düştükçe kalite artar

cap.release() #videoyu kapatır ve üzerinde işlem yapmaya müsait hale getirir
cv2.destroyAllWindows()
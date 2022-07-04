import cv2

cap = cv2.VideoCapture(0)

def nothing(x):
    pass
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",(500,150))

cv2.createTrackbar("Lower-TH","Trackbar",0,255,nothing)

cv2.createTrackbar("Upper-TH","Trackbar",0,255,nothing)

cv2.setTrackbarPos("Upper-TH","Trackbar",255)

while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    TH1 = cv2.getTrackbarPos("Lower-TH", "Trackbar")

    TH2 = cv2.getTrackbarPos("Upper-TH", "Trackbar")

    frame = cv2.Canny(frame,TH1,TH2)

    cv2.imshow("Webcam",frame)
    cv2.waitKey(30)

cap.release()
cv2.destroyAllWindows()
import cv2

yakala = cv2.VideoCapture("Video1.mp4")

while True:
    ret,frame = yakala.read()
    frame1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    if ret == 0:
        break

    cv2.imshow("Video1",frame1)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

yakala.release()
cv2.destroyAllWindows()
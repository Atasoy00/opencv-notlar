import cv2

cap = cv2.VideoCapture(0)
circles = []
#lines = []


def mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x, y))
        #lines.append((x,y+10))

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse)

while 1:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))

    for center in circles:
        cv2.circle(frame, center, 10, (0, 255, 255), -1)
        #for line in lines:
         #   cv2.line(frame,center,line,(0,255,255),2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("h"): #temizleme tusu
        circles = []

cap.release()
cv2.destroyAllWindows()





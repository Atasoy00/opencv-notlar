import cv2

img0 = cv2.imread("face.png")

face_cascade = cv2.CascadeClassifier("FrontalFace_HaarCascade.xml")

img = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img,1.3,6)

for (x,y,w,h) in faces:
    cv2.rectangle(img0,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Pencere",img0)
cv2.waitKey(0)
cv2.destroyAllWindows()
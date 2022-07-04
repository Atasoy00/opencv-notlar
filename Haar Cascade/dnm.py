import cv2

vid = cv2.VideoCapture(0)

petSise_cascade = cv2.CascadeClassifier("Eye_HaarCascade.xml")

while 1:

    ret, frame = vid.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (480, 360))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    petSiseler = petSise_cascade.detectMultiScale(gray,1.7,6)

    for (x, y, w, h) in petSiseler:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('video', frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()

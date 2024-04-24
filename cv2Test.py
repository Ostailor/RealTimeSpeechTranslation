import numpy as np
import cv2 as cv

# Load the Haar cascade classifier for face detection
faceCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the Haar cascade classifier for mouth detection
# Note: You might need to use an absolute path to the Haar cascade XML file for the mouth
#Does not work????
mouthCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_mcs_mouth.xml')

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Convert the frame to grayscale for face detection
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Convert the face region to grayscale for mouth detection
        face_gray = gray[y:y+h, x:x+w]

        # Detect mouths in the face region
        mouths = mouthCascade.detectMultiScale(face_gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))

        # Draw a rectangle around the mouths
        for (mx, my, mw, mh) in mouths:
            cv.rectangle(frame, (x+mx, y+my), (x+mx+mw, y+my+mh), (255, 0, 0), 2)

    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

from __future__ import print_function
import cv2 as cv
import argparse
def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)


    #Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)

    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]

        #In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)

        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)

    cv.imshow('Detector', frame)


face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()
#Load cascades and quit if not loading
if not face_cascade.load(cv.samples.findFile('data/haarcascades/haarcascade_frontalface_alt.xml')):
    print('! NO FACE CASCADE FILE')
    exit(0)
if not eyes_cascade.load(cv.samples.findFile('data/haarcascades/haarcascade_eye.xml')):
    print('! NO EYES CASCADE FILE')
    exit(0)
#Get incoming video stream from webcam
cap = cv.VideoCapture(0)
if not cap.isOpened:
    print('! NO CAPTURE')
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('! NO FRAME')
        break
    detectAndDisplay(frame)
    if cv.waitKey(10) == 27:
        break
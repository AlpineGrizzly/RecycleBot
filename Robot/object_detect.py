from __future__ import print_function
import cv2 as cv
import argparse

#For testing and visualization purposes
def detectAndDisplay(frame):

    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    #Detect cans and bottles
    cans = can_cascade.detectMultiScale(frame_gray)
    bottles = bottle_cascade.detectMultiScale(frame_gray)

    #Draw rectangle on each can and bottle
    for (x,y,w,h) in cans:
        top_left = (x, y)
        bottom_right = (x+w, y+h)
        frame = cv.rect(frame, top_left, bottom_right, '#F01010', 2, cv.LINE_8, 0)
    for (x,y,w,h) in bottles:
        top_left = (x, y)
        bottom_right = (x+w, y+h)
        frame = cv.rect(frame, top_left, bottom_right,  '#10F010', 2, cv.LINE_8, 0)

    cv.imshow('Detector', frame)

#For use with robot, gives tuple with two arrays, cans and bottles. Each array contains the x and y of the top left, as well as the width and height
def detect(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    #Detect cans and bottles
    cans = can_cascade.detectMultiScale(frame_gray)
    bottles = bottle_cascade.detectMultiScale(frame_gray)
    print("Cans: " + str(len(cans)) + " | Bottles: " + str(len(bottles)))
    return (cans, bottles)

can_cascade = cv.CascadeClassifier()
bottle_cascade = cv.CascadeClassifier()
#Load cascades and quit if not loading
if not can_cascade.load(cv.samples.findFile('data/haarcascades/haarcascade_can.xml')):
    print('! NO CAN CASCADE FILE')
    exit(0)
if not bottle_cascade.load(cv.samples.findFile('data/haarcascades/haarcascade_bottle.xml')):
    print('! NO BOTTLE CASCADE FILE')
    exit(0)

try:
	cap = cv.VideoCapture(0)
	if not cap.isOpened:
		print('! NO CAPTURE')
		exit(0)
	while True:
		ret, frame = cap.read()
		if frame is None:
			print('! NO FRAME DATA')
			break
		detect(frame)
except KeyboardInterrupt:
	print('PROCESS STOPPED')

##Get incoming video stream from webcam
#cap = cv.VideoCapture(0)
#if not cap.isOpened:
#    print('! NO CAPTURE')
#    exit(0)
#while True:
#    ret, frame = cap.read()
#    if frame is None:
#        print('! NO FRAME')
#        break
#    detectAndDisplay(frame)
#    if cv.waitKey(10) == 27:
#        break

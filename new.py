import math
import cv2
import numpy as np
import sys

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    for xf,yf,wf,hf in faces:
        frame_f=frame[xf:xf+wf,yf:yf+hf]
        gray_f = cv2.cvtColor(~frame_f, cv2.COLOR_BGR2GRAY)
        ret, thresh_gray = cv2.threshold(gray_f, 220, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.rectangle(frame, (xf, yf), (xf+wf, yf+hf), (0, 255, 0), 2)

        # for contour in contours:
        #     area=cv2.contourArea(contour)
        #     rect=cv2.boundingRect(contour)
        #     x, y, width, height =rect
        #     radius =0.25*(width+height)
        #
        #     area_condition = (100 <=area <=200)
        #     symmetry_condition = (abs(1-float(width)/float(height)) <=0.2)
        #     fill_condition = (abs (1-(area/(math.pi*math.pow(radius, 2.0))))<=0.3)
        #
        #     if area_condition and symmetry_condition and fill_condition:
        #         cv2.circle(frame,(int(x+radius),int(y+radius)),int(1.3*radius),(0,180,0),-1)

    cv2.imshow('pupil',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()

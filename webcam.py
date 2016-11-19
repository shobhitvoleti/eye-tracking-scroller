import cv2
import sys
import numpy as np

# TO DO: Make this a function. Make main.py after pdf gets sorted out, then send frame to this function and return eye coordinates.
eyeCascade = cv2.CascadeClassifier('./haarcascade_eye_2.xml')
faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

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
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
    area=[]
    fc=[0,0,500,500]
    xe=0
    ye=0
    f2=frame
    for (x,y,w,h) in faces:
        area.append(([x,y,w,h],h*w))
        y_wind=frame.shape[1]
        x_wind=frame.shape[0]
        #cv2.rectangle(frame, (0,0), (1280,720), (0, 255, 0), 2)
        #cv2.rectangle(frame, (0,0), (900,900), (0, 255, 0), 2)
        #cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        #cv2.rectangle(frame, (0,y_wind-1100), (200,y_wind-900), (0, 255, 0), 2)
        #f2=frame[y:y+h,x:x+w]

    if area:
        face_tracked=sorted(area,key=lambda x:x[1],reverse=True)[0][0]
        face_gray=gray[face_tracked[1]:face_tracked[1]+face_tracked[3],face_tracked[0]:face_tracked[0]+face_tracked[2]]
        eyes = eyeCascade.detectMultiScale(
            face_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
        for (x, y, w, h) in eyes:
            xe=x+w/2
            ye=y+h/2
            cv2.circle(frame, (xe+face_tracked[0],ye+face_tracked[1]),2, (0,255,0),8)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    #f3=frame[fc[0]:fc[0]+fc[2],fc[1]:fc[1]+fc[3]]
    #cv2.namedWindow('frame2', cv2.WINDOW_NORMAL)
    #cv2.imshow('frame2', f3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows

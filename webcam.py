import cv2
import sys
import numpy as np
#TODo make function
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
    # Draw a rectangle around the eyes
    xe=0
    ye=0
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        crpped=gray[x:x+w,y:y+h]
        xe=x+w/2
        ye=y+h/2
        cv2.circle(frame, (xe,ye),2, (0,255,0),8)
        #circles = cv2.HoughCircles(crpped,cv2.cv.CV_HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
        # if circles is not None:
        #     circles = np.round(circles[0, :]).astype("int")
        #     for (xc, yc, rc) in circles:
        #         cv2.circle(frame, (x+xc, y+yc), rc, (0, 255, 0), 4)
        #         cv2.rectangle(frame, (x+xc - 5, y+yc - 5), (xc + 5, yc + 5), (0, 128, 255), -1)


    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows

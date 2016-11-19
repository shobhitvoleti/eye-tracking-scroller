import cv2
import sys
import numpy as np

# TO DO: Make this a function. Make main.py after pdf gets sorted out, then send frame to this function and return eye coordinates.

def get_face(faces):
    area=[]
    if not type(faces) == 'tuple':
        for (x,y,w,h) in faces:
            area.append(([x,y,w,h],h*w))
        if area:
            face_to_track=sorted(area,key=lambda x:x[1],reverse=True)[0][0]
            return face_to_track
        else:
            return None
    else:
        return None

def get_eyes(eyes):
    if not type(eyes) == 'tuple':
        xe=0
        ye=0
        for (x, y, w, h) in eyes:
            xe=xe+x+w/2
            ye=ye+y+h/2
            #cv2.circle(frame, (xe+face_tracked[0],ye+face_tracked[1]),2, (0,255,0),8)
        return (xe/2,ye/2)
        else:
            return (0,0)


def call_for_eyecoords(frame):
    eyeCascade = cv2.CascadeClassifier('./haarcascade_eye_2.xml')
    faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    eye_coords=(0,0)
    #video_capture = cv2.VideoCapture(0)

# while True:
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

    face_tracked=get_face(faces)

    if face_tracked is not None:
        face_gray=gray[face_tracked[1]:face_tracked[1]+face_tracked[3],face_tracked[0]:face_tracked[0]+face_tracked[2]]
        eyes = eyeCascade.detectMultiScale(
            face_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

        eye_coords=get_eyes(eyes)
    return eye_coords
    # Display the resulting frame
    # cv2.imshow('frame', frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        # break

# When everything is done, release the capture
# video_capture.release()
# cv2.destroyAllWindows

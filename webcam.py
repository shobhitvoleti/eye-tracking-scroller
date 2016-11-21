import cv2
import sys
import numpy as np

# TO DO: Make this a function. Make main.py after pdf gets sorted out,
# then send frame to this function and return eye coordinates.
eyeCascade = cv2.CascadeClassifier('./haarcascade_eye_2.xml')
faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_coords = (0, 0)


def get_face(faces):
    """
    Function to find most prominent face among a set of faces in a frame

    Input :
        faces : numpy.ndarray
            Array of rectangles that bound the faces obtained post processing the image

    Return : tuple
        Coordinates of opposite corners of the rectangle that bounds the most prominent face
    """
    area = []
    if not type(faces) == 'tuple':
        for (x, y, w, h) in faces:
            area.append(([x, y, w, h], h * w))
            #cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 0), 2)
        if area:
            face_to_track = sorted(
                area, key=lambda x: x[1], reverse=True)[0][0]
            return face_to_track
        else:
            return ([-2000,-2000,-2000,-2000],-2000)
    else:
        return ([-2000,-2000,-2000,-2000],-2000)


def get_eyes(eyes, fd):
    """
    Function to find coordinates of eyes in a face obtained from the frame

    Input :
        eyes : numpy.ndarray
            Array of rectangles that bound the eyes obtained post processing the image

    Return : tuple
        Coordinates of opposite corners of the rectangle that bounds the eyes
    """
    if not type(eyes) == 'tuple':
        xe = 0
        ye = 0
        for (x, y, w, h) in eyes:
            xe = xe + x + w / 2
            ye = ye + y + h / 2
            #cv2.circle(frame, (x+face_tracked[0]+w/2,y+face_tracked[1]+h/2),2, (0,255,0),8)
        if not len(eyes) == 0:
            xe = xe / len(eyes) + fd[0]
            ye = ye / len(eyes) + fd[1]
            # cv2.circle(frame, (xe,ye),2, (0,255,0),8)
            return (xe, ye)
        else:
            return (-2000,-2000)
    else:
        return (-2000,-2000)


def call_for_eyecoords(frame):
    """
    Function that processes the image using classifiers and returns positions of the centres of the eyes and faces

    Input :
        frame : numpy.ndarray
            An RGB array of pixels that describe a frame of the video feed

    Return : tuple
        Positions of the centres of the eyes and face
    """

    eye_coords=[-2000,-2000]
    xf=-2000
    yf=-2000

    if not isinstance(frame, np.ndarray):
        raise TypeError('Object not recognized by cv2, not an array!')
    else:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30))
            #flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
        face_tracked = get_face(faces)
        if not face_tracked == ([-2000,-2000,-2000,-2000],-2000):
            face_gray = gray[
                face_tracked[1]:face_tracked[1] +
                face_tracked[3],
                face_tracked[0]:face_tracked[0] +
                face_tracked[2]]
            eyes = eyeCascade.detectMultiScale(
                face_gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30))
                #flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
            eye_coords = get_eyes(eyes, face_tracked)
            xf = face_tracked[0] + face_tracked[2] / 2
            yf = face_tracked[1] + face_tracked[3] / 2
        else:
            xf = -2000
            yf = -2000
        return (eye_coords[0], eye_coords[1], xf, yf)
        # Display the resulting frame
    # cv2.imshow('frame', frame)
    # cv2.waitKey(5000)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break
if __name__ == '__main__':
    pass

# When everything is done, release the capture
# video_capture.release()
# cv2.destroyAllWindows

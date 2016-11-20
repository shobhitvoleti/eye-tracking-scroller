import cv2
import webcam as wbc
import nod_scroll as ns
import numpy as np
import pickle

while True:
    video = cv2.VideoCapture(0)
    ret, frame = video.read()
    positions = wbc.call_for_eyecoords(frame)
    x_avg_face = 0
    y_avg_eyes = 0
    x_window_face = [-2000]
    y_window_eyes = [-2000]

    if len(y_window_eyes) <= 10:
        if not positions[1] == -2000:
            if y_window_eyes == -2000:
                y_window_eyes[:] = []
                y_window_eyes.append(positions[1])
            else:
                y_window_eyes.append(positions[1])
    else:
        y_avg_eyes = np.mean(y_window_eyes) / 3 + y_avg_eyes * 2 / 3
        y_window_eyes[:] = [-2000]

    if len(x_window_face) <= 10:
        if not positions[2] == -2000:
            if x_window_face == -2000:
                x_window_face[:] = []
                x_window_face.append(positions[1])
            else:
                x_window_face.append(positions[1])
    else:
        x_avg_face = np.mean(x_window_face) / 3 + x_avg_face * 2 / 3
        x_window_face[:] = [-2000]

    scroll_flag = ns.scroll_pdf(y_avg_eyes, y_window_eyes)
    nod_flag=ns.next_page(x_avg_face,x_window_face)

    pickle.dump( scroll_flag, open( "save.p", "wb" ) )

video.release()

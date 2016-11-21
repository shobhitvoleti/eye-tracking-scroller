x_avg_face = 0
y_avg_eyes = 0
x_window_face = [-2000]
y_window_eyes = [-2000]



    video = cv2.VideoCapture(0)
    ret, frame = video.read()
    positions = wbc.call_for_eyecoords(frame)
    # if len(x_window_face)<=10:
    #     if not positions[2] == -2000 :
    #         x_window_face.append(positions[2])
    # else:
    #     x_avg_face=np.mean(x_window_face)/3+x_avg_face*2/3
    #     x_window_face[:]=[]

    if len(y_window_eyes) <= 10:
        if not positions[1] == -2000:
            if y_window_eyes == -2000:
                y_window_eyes[:] = []
                y_window_eyes.append(positions[1])
            else:
                y_window_eyes.append(positions[1])

    else:
        y_avg_face = np.mean(y_window_eyes) / 3 + y_avg_eyes * 2 / 3
        y_window_eyes[:] = [-2000]

    # nod_flag=ns.next_page(x_avg_face,x_window_face)
    scroll_flag = ns.scroll_pdf(y_avg_eyes, y_window_eyes)

    # if nod_flag == 1:
    #     button1.invoke()
    # elif nod_flag == -1:
    #     button4.invoke()
    if scroll_flag == 1:
        button3.invoke()
    elif scroll_flag == -1:
        button2.invoke()

video.release()

if __name__ == "__main__":
    pass

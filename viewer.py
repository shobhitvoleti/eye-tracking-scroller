from Tkinter import *
from PIL import Image, ImageTk
import pypdfocr.pypdfocr_gs as pdfImg
import ttk
import glob
import os
from pdfui import fname
import cv2
import sys
import numpy as np
import webcam as wbc
import nod_scroll as ns


root = Tk()
canv = Canvas(root, height=1500, width=1000)
canv.pack(side=LEFT, fill=BOTH)

# Generating and processing initial image from PDF
my_img = glob.glob(pdfImg.PyGs({}).make_img_from_pdf(fname)[1])[0]
im = Image.open(my_img)
width1, height1 = im.size
resized = im.resize((1000, height1 / 2), Image.ANTIALIAS)
width, height = resized.size
im2 = ImageTk.PhotoImage(resized)
a1 = canv.create_image(0, 0, anchor="nw", image=im2)

# Declaring array filled with images
imglen = len(glob.glob(pdfImg.PyGs({}).make_img_from_pdf(fname)[1]))
imgarr = []
for i in range(imglen):
    imgarr.append(glob.glob(pdfImg.PyGs({}).make_img_from_pdf(fname)[1])[i])

imarr = []
for i in imgarr:
    imarr.append(Image.open(i))
width1, height1 = imarr[0].size

# Rearranging images to fit window
rearr = []
for i in imarr:
    rearr.append(i.resize((1000, height1 / 2), Image.ANTIALIAS))
width, height = rearr[0].size

finarr = []
for i in rearr:
    finarr.append(ImageTk.PhotoImage(i))


def movedown():
    canv.yview_scroll(2, 'units')

    button2.place(relx=0.0, rely=1.0, anchor=SW)
    button1.place(relx=0.0, rely=0.0, anchor=NW)
    button4.place(relx=1.0, rely=1.0, anchor=SE)
    button3.place(relx=1.0, rely=0.0, anchor=NE)
    button5.place(relx=0.5, rely=0.5, anchor=SE)

    pass


def moveup():
    canv.yview_scroll(-2, 'units')
    button2.place(relx=0.0, rely=1.0, anchor=SW)
    button1.place(relx=0.0, rely=0.0, anchor=NW)
    button4.place(relx=1.0, rely=1.0, anchor=SE)
    button3.place(relx=1.0, rely=0.0, anchor=NE)
    button5.place(relx=0.5, rely=0.5, anchor=SE)

    pass


def quit():

    root.quit()

image_number = 0


def changepage():
    global image_number
    image_number += 1

    if image_number == imglen:
        image_number = 0

    canv.itemconfig(a1, image=finarr[image_number])


def prevpage():
    global image_number
    if image_number == 0:
        image_number = imglen - 1
    else:
        image_number -= 1
    canv.itemconfig(a1, image=finarr[image_number])

def webb():
    video = cv2.VideoCapture(0)
    ret, frame = video.read()
    positions = wbc.call_for_eyecoords(frame)


button1 = Button(canv, text="Nextpage", command=changepage, anchor=W)
button1.configure(width=10, activebackground="#33B5E5", relief=FLAT)
button1_window = canv.create_window(10, 10, anchor=NW, window=button1)

button2 = Button(canv, text="movedown", command=movedown, anchor=W)
button2.configure(width=10, activebackground="#33B5E5", relief=FLAT)
button2_window = canv.create_window(200, 10, anchor=NW, window=button2)

button3 = Button(canv, text="moveup", command=moveup, anchor=W)
button3.configure(width=10, activebackground="#33B5E5", relief=FLAT)
button3_window = canv.create_window(400, 10, anchor=NW, window=button3)

button4 = Button(canv, text="prevpage", command=prevpage, anchor=W)
button4.configure(width=10, activebackground="#33B5E5", relief=FLAT)
button4_window = canv.create_window(600, 10, anchor=NW, window=button4)

button5 = Button(canv, text="quit", command=quit, anchor=W)
button5.configure(width=10, activebackground="#33B5E5", relief=FLAT)
button5_window = canv.create_window(900, 10, anchor=NW, window=button5)

button6 = Button(canv, text="haaar", command=webb, anchor=W)
button6.configure(width=10, activebackground="#33B5E5", relief=FLAT)
button6_window = canv.create_window(900, 10, anchor=NW, window=button6)


mainloop()
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

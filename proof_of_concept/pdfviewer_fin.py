from Tkinter import *
from PIL import Image, ImageTk
import pypdfocr.pypdfocr_gs as pdfImg
import ttk
import glob
import os
from pdfui import fname
import pickle




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
    """
    Function that executes scroll

    Description :
        Moves canvas down by 2 units and sets buttons in place

    """
    canv.yview_scroll(2, 'units')

    button2.place(relx=0.0, rely=1.0, anchor=SW)
    button1.place(relx=0.0, rely=0.0, anchor=NW)
    button4.place(relx=1.0, rely=1.0, anchor=SE)
    button3.place(relx=1.0, rely=0.0, anchor=NE)
    button5.place(relx=0.5, rely=0.5, anchor=SE)

    pass


def moveup():
    """
    Function that executes scroll

    Description :
        Moves canvas up by 2 units and sets buttons in place

    """
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
    """
    Function that executes next page function

    Description :
        Changes image on canvas to display new page

    """
    global image_number
    image_number += 1

    if image_number == imglen:
        image_number = 0

    canv.itemconfig(a1, image=finarr[image_number])


def prevpage():
    """
    Function that executes next page function

    Description :
        Changes image on canvas to display new page

    """
    global image_number
    if image_number == 0:
        image_number = imglen - 1
    else:
        image_number -= 1
    canv.itemconfig(a1, image=finarr[image_number])

#def initiali():
#    with open('randi.pickle', 'rb') as f:
        # The protocol version used is detected automatically, so we do not
        # have to specify it.



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

perm = pickle.load( open( "save.p", "rb" ) )

if perm == 0:
    button2.invoke()
    print "my proof of concept"


mainloop()
if __name__ == "__main__":
    pass

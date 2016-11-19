import pypdfocr.pypdfocr_gs as pdfImg
from PIL import Image, ImageTk
from Tkinter import Label, Frame
import Tkinter as tk
import ttk
import glob, os

class MyImage(Frame):
    def __init__(self, master = None):

        Frame.__init__(self, master)
        self.pack()
        w = 1500; h = 1000


        x = (self.master.winfo_screenwidth())/2
        y = (self.master.winfo_screenheight())/2

        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        __f_tmp=glob.glob(pdfImg.PyGs({}).make_img_from_pdf("Tkinter.pdf")[1])[0]
        #                             ^ this is needed for an "default"-Config
        img=Image.open(__f_tmp)
        pic = ImageTk.PhotoImage(img)
        label = Label(self, image = pic)
        label.image = pic
        label.pack()


    def showEnd(event):
        img.see(tk.END)
        img.edit_modified(False) #IMPORTANT - or <<Modified>> will not be called later.

if __name__ == "__main__":

    MyImage().mainloop()

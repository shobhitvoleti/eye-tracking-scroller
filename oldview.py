import pypdfocr.pypdfocr_gs as pdfImg
from PIL import Image, ImageTk
import Tkinter as tk
import ttk
import glob, os

root=tk.Tk()

__f_tmp=glob.glob(pdfImg.PyGs({}).make_img_from_pdf("test.pdf")[1])[0]
#                             ^ this is needed for an "default"-Config
__img=Image.open(__f_tmp)

__tk_img=ImageTk.PhotoImage(__img)

ttk.Label(root, image=__tk_img).grid()

__img.close()
os.remove(__f_tmp)

root.mainloop()

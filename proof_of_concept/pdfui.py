from Tkinter import *
import tkFileDialog
import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk


def browse_file():
    global fname
    fname = tkFileDialog.askopenfilename(filetypes=(
        ("PDF files", "*.pdf"), ("All files", "*")))

root = Tk.Tk()
root.wm_title("Browser")
broButton = Tk.Button(master=root, text='Browse', width=6, command=browse_file)
broButton.pack(side=Tk.LEFT, padx=2, pady=2)

Tk.mainloop()

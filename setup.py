import sys
from setuptools import setup, find_packages

requires = ["numpy","cv2","pypdfocr","Tkinter","glob","ttk","PIL"]

setup(
        name="VisualScrollingAid",
        version="1.0",
        description="Scroll through PDF optically",
        url="https://github.com/shobhitvoleti/eye-tracking-scroller",
        author="Shobhit Voleti","Siddharth Nair"
        author_email="shobhitvoleti@gmail.com, siddharth.nair@iitb.ac.in",
        license="GPL3",
        install_requires=requires,
        packages=find_packages(),
        )

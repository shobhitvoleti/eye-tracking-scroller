Welcome to VSA's Repository!
========================


Built as a proof of concept of a webcam based eye tracker using Python's **OpenCV and TkInter** 

----------


Description
-------------

Below is a description of both halves of the whole


>  **Webcam Pupil Detection**
>
> -  XML file contains cascade of tests (Haar's Cascade) which check whether object in a moving window is a face or not
> -  Create an object that uses the tests in the .xml file to extract faces from images sampled from webcam feed
> -  Localize eyes using empirical data and  Haar's Cascade.
> -  Identity the most prominent face in a frame and use Haar's Cascade to obtain the location of the eyes.


> **PDF Viewer using Tkinter**

> -  Created a canvas on a window of fixed dimensions
> -  Implemented yview.scroll and button placements to achieve scrolling in y direction
> -  Processed images to make a PDF fit in the x direction always
> -  Implemented custom function and image arrays to systematically remove and display page by page of a PDF on the click of a button.


#### <i class="icon-file"></i> Installation

The dependancies can be installed by running 
> python setup.py build

> python setup.py install

On the command line or Terminal

#### <i class="icon-folder-open"></i> Switch between tools

Both the tools are available separately on GitHub open source for use 


----------

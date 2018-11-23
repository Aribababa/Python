# Bus route detection for blind people.

## Objective

Use the knowledge seen in class and within the area of computer vision systems to know how to design and implement this type of systems under controlled conditions and in real environments.

## Problematic

Currently, the Mexican government does very little for people with visual disabilities, so a device that helps them take public transport will be very useful for them. In some cities of the Mexican Republic, they have facilities that help people with visual disabilities to be more easily guided at the time of walking, but currently, it is difficult to reach our destination simply by walking, that is why helping them to use transportation public to provide them with some of their problems.

## Solution

The project consists of integrating a system that recognizes urban trucks in the street, that identifies which route is and so, that helps blind people to be more independent when using public transport. This thanks to the development of a tool that uses image processing for route detection.

## Importing the libraries
This project need some libraries to be excetuded. In most fo the cases all the libaries can be installed using pip command from Python.

    ../UserName> python -m pip [install | uninstall] <library name>

The following libraries are required:
```python
import cv2
import numpy as np
from  PIL  import Image
import pytesseract
```

## Installing Tesseract
In the case of PyTesseract, Tesseract OCR needs to be installed first. It is recommended to use Tesseract 3.4. You can either [Install Tesseract via pre-built binary package](https://github.com/tesseract-ocr/tesseract/wiki) or [build it from source](https://github.com/tesseract-ocr/tesseract/wiki/Compiling).

## Running the project.
Once the librearies were installed correctly, just simply run RouteDetection.py and be sure that all the XML files are in the same folder.

    ../Scripts> python RouteDetection.py 
    
A window will open in your desktop with the frames capturer by your camera.
<p align="center">
  <img src="https://lh3.googleusercontent.com/fQFU8eL0DY3VWb9r12gxxTiN9pI9PUnj7HqhaQMBokNL4IIIBxieaZn_MrtVe2B_RjUCb-Ru0Jl1hZxiYQhlKomgeH8qxIm5NvfL87sp1yvS9hIpUA1Y3UEA5ZiL7e-112U-LMTv">
</p>
When a bus is in the frames for a certain number of frames, the Script will crop the object and then it will porgress to process the Data.
At the end, An image will be created in the same folder as the .py file with the route processed and the Script will dictate the route.

## Video
To see the project running, pleae go to the link below.
[Route Detection Video](https://www.youtube.com/watch?v=mo6xxib4ots&feature=youtu.be)

## Future work.

 -   The main problem here is the Cascade file. When the classifier has being made, we do not consider some special cases for the buses, more specifically the *SiTren* Route in Guadalajara. Training a new classifier with the other buses and give them more states to the algorithm will increase the accuracy and the precision,
 
 - Other issue with the Script is the FrameRate where is dependent of the device where the files are executed. Limit this rate could improve the detectin time.

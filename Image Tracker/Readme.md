# Image Tracker with OpenCV and Arduino

## How it works
There are at least 7 types of tracker algorithms that can be used:

-   MIL
-   BOOSTING
-   MEDIANFLOW
-   TLD
-   KCF
-   GOTURN
-   MOSSE

Each tracker algorithm has their own advantages and disadvantages,
Using this function, you can select the bounding box of the tracked object using a GUI. With default parameters, the selection is started from the center of the box and a middle cross will be shown.

With the reference of our object, we can obtain the centre  and normalize the position values in a range of [0, 255] to send it via Serial to our Microcontroller.

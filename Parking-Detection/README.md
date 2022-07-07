# PARKING DETECTION
This Parking detection project is very simple to understand, it doesn't use deep learning like Yolo v3, Yolo v4 even the newest Yolo. This parking detection uses the image processing method, which uses a threshold value to determine whether or not there are cars in the parking lot.

flow :
- In the createRectangle directory there is a parkingSpacePicker.py file. This file is a class that is used to create or mark a parking rectangle. To run it running the main.py file which is in the createRectangle directory, this class will return an object list.

- Image Processing
   1. Convert video from RGB to grayscale
   2. Convert grayscal to gausianBlur
   3. Convert gausianblur to medianBlur
   4. Convert medianBlur to dilate
 
- Analyze objects that have been marked then calculate threshold


Happy reading

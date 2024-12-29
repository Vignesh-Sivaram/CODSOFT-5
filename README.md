# Face detection and recognition

## Overview
* This project demonstrates face recognition feature of program in a given image or in a live video by OpenCV, a library.
The program employs Haar Cascade Classifier, a machine learning object detection method, to identify faces.

## Key Components:

### 1) Importing Libraries:

* cv2: OpenCV library for image and video processing.
* matplotlib.pyplot: For displaying images.
* time: For handling time-related functions.

### 2) Function: detect_face_in_image(image_path):

* Read Image: Loads the image from the specified path using cv2.imread().
* Convert to Grayscale: Converts the image to grayscale using cv2.cvtColor(), as face detection works better on grayscale images.
* Load Haar Cascade Classifier: Loads the pre-trained Haar Cascade Classifier for frontal face detection.
* Detect Faces: Uses detectMultiScale() to detect faces in the grayscale image. This function returns a list of rectangles where faces are detected.
* Draw Rectangles: Draws rectangles around detected faces using cv2.rectangle().
* Convert to RGB: Converts the image back to RGB for displaying with Matplotlib.
* Display Image: Uses Matplotlib to display the image with detected faces.
  
### 3) Function: detect_face_live():

* Load Haar Cascade Classifier: Loads the pre-trained Haar Cascade Classifier for frontal face detection.
* Open Video Capture: Opens the webcam using cv2.VideoCapture(0).
* Check Video Capture: Checks if the webcam is opened successfully.
* Set Duration: Sets the duration for the live video capture.
* Start Time: Records the start time.
* Capture Frames: Continuously captures frames from the webcam.
  * Convert to Grayscale: Converts each frame to grayscale.
  * Detect Faces: Uses detectMultiScale() to detect faces in the grayscale frame.
  * Draw Rectangles: Draws rectangles around detected faces.
  * Display Frame: Displays the frame with detected faces using cv2.imshow().
  * Exit Condition: Exits the loop if 'q' is pressed or the duration is exceeded.
* Release Resources: Releases the webcam and closes all OpenCV windows.

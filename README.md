
# Face Tracking

## Overview

This repository provides a tutorial for implementing real-time face tracking using OpenCV and Python. The tutorial covers setting up the environment, understanding the code, and running the face tracking application.

## Features

- Real-time face detection and tracking using Haar cascades and CSRT trackers.
- Efficient tracker management to handle multiple faces.
- Live demonstration of face tracking through webcam.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- OpenCV library

You can install the necessary Python libraries using `pip`:

```bash
pip install opencv-python
```

## Getting Started

Follow these steps to get the face tracking application running on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/adityadwi21/FaceTracking.git
cd FaceTracking
```

### 2. Run the Face Tracking Application

Run the `app.py` script to start the face tracking application:

```bash
python app.py
```

### 3. Stopping the Application

To stop the application, press the 'q' key in the application window.

## Code Explanation

Here's a brief overview of how the code works:

1. **Face Detection**: Uses Haar cascade classifier to detect faces in each frame.
2. **Tracking**: Initializes CSRT trackers for detected faces and updates their positions in subsequent frames.
3. **Visualization**: Draws bounding boxes around tracked faces and displays the video feed with face tracking.

### Key Sections

- **Face Detection**: `face_cascade.detectMultiScale()`
- **Tracker Initialization**: `cv2.TrackerCSRT_create()`
- **Tracker Update**: `tracker.update()`

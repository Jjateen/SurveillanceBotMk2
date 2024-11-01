---

# Surveillance Bot Mk2

## [Demo Video](https://www.linkedin.com/posts/jjateen_ai-ml-electronics-activity-7143582599070818305-wCSS?utm_source=share&utm_medium=member_desktop)

Surveillance Bot Mk2 is an advanced AI semi-autonomous robot designed for cutting-edge surveillance applications. This repository contains the code and documentation for the project.

## Features

- **Wireless Control:** Navigate the robot wirelessly through a user-friendly web app joystick.
- **Object Detection:** Real-time object detection powered by the MobileNetSSD network.
- **Image Collection:** Utilizes ESP32CAM to collect high-quality images via a local Flask webserver and GET requests.
- **Live Video Feed:** Experience the future with a live video feed displaying object detection on the sleek web app interface.

## MobileNetSSD Caffe Model

The MobileNetSSD (Single Shot Detector) is a deep learning model specifically designed for efficient object detection. This network is trained using the Caffe deep learning framework, and it's optimized for embedded devices such as ESP32CAM, ensuring low-latency, real-time performance.

MobileNetSSD can detect multiple objects such as people, vehicles, and common objects, making it ideal for surveillance applications. The **MobileNetSSD_deploy.caffemodel** file contains the pre-trained model weights, while **MobileNetSSD_deploy.prototxt.txt** defines the architecture of the network.

For more information about how the MobileNetSSD model works, you can explore the [Caffe Model Zoo](https://github.com/BVLC/caffe/wiki/Model-Zoo).

## Getting Started

Follow these steps to get Surveillance Bot Mk2 up and running:

### 1. Install Dependencies

Ensure you have all the necessary Python libraries installed. You can install them from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 2. Set Up ESP32CAM

- Configure your ESP32CAM module and ensure it's connected to the robot.
- Flash the appropriate firmware to allow the camera to stream video and capture images.
- Confirm that the camera module is properly aligned with the bot for clear video feed.

### 3. Run Flask Webserver

To enable image collection, run the Flask web server, which will handle incoming GET requests from the ESP32CAM:

```bash
flask run
```

This will start a local web server, where the camera feed can be accessed in real-time.

### 4. Launch the Web App

Open the provided web application in your browser. This interface allows you to control the robot remotely using a joystick and displays the live video feed with real-time object detection powered by the MobileNetSSD model.

### 5. Tutorial: Object Detection and Surveillance Setup

1. **Object Detection Integration:** 
   - The MobileNetSSD model has been integrated into the robot's system to provide real-time object detection.
   - The web interface not only displays the video feed but also highlights detected objects with bounding boxes and labels.

2. **ESP32CAM Configuration:**
   - Ensure that the ESP32CAM module is connected to your local Wi-Fi network. This allows it to stream data to the Flask server, which then processes the frames using MobileNetSSD.

3. **Web App Control:**
   - Navigate the robot through the web app using the joystick and monitor the live feed simultaneously. This allows you to spot objects and navigate the bot accordingly.
   
4. **Image Storage:** 
   - Captured images are stored locally, and you can retrieve them for further analysis or log them for security purposes.

### 6. Testing and Calibration

To ensure smooth operation, test the ESP32CAM’s connectivity and object detection by navigating the robot around your environment. Adjust the camera angles or parameters based on the lighting conditions for optimal performance.

## Usage

- Connect to the robot's web app interface and use the joystick for wireless control.
- View the live video feed with real-time object detection.
- Capture and store images for review.

## Contributing

Feel free to contribute by submitting issues, feature requests, or pull requests. Your feedback is valuable!

---

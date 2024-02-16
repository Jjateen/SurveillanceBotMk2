# Surveillance Bot Mk2

Surveillance Bot Mk2 is an advanced AI semi-autonomous robot designed for cutting-edge surveillance applications. This repository contains the code and documentation for the project.

## Features

- **Wireless Control:** Navigate the robot wirelessly through a user-friendly web app joystick.
- **Object Detection:** Real-time object detection powered by the MobileNetSSD network.
- **Image Collection:** Utilizes ESP32CAM to collect high-quality images via a local Flask webserver and GET requests.
- **Live Video Feed:** Experience the future with a live video feed displaying object detection on the sleek web app interface.

## Getting Started

Follow these steps to get Surveillance Bot Mk2 up and running:

1. **Install Dependencies:** Check the requirements.txt file for necessary Python libraries.
   ```bash
   pip install -r requirements.txt
   ```

2. **ESP32CAM Setup:** Configure your ESP32CAM module and ensure it is connected to the robot.

3. **Run Flask Webserver:** Start the Flask webserver for image collection.
   ```bash
   flask run
   ```

4. **Launch Web App:** Open the web app on your preferred browser and take control of the robot!

## Usage

- Connect to the robot's web app interface and use the joystick for wireless control.
- View the live video feed with real-time object detection.

## Contributing

Feel free to contribute by submitting issues, feature requests, or pull requests. Your feedback is valuable!

from flask import Flask, render_template, Response
import cv2
import numpy as np
import requests

app = Flask(__name__)

prototxt = "MobileNetSSD_deploy.prototxt.txt"
model = "MobileNetSSD_deploy.caffemodel"
confThresh = 0.6

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

print("Loading model...")
net = cv2.dnn.readNetFromCaffe(prototxt, model)
print("Model Loaded")

# url = "http://192.168.4.1:81/stream"
url = "http://192.168.1.16:81/stream"

# Define robot control functions
# these will probably be get requests defined on ESP32-CAM's routes
def forward():
    pass

def backward():
    pass

def left():
    pass

def right():
    pass

def stop():
    pass

def cat_follower_logic(x_center, y_center, image_width, image_height):
    # Define safe zone dimensions
    safe_zone_width = 100  # Adjust according to your robot's capabilities
    safe_zone_height = 100  # Adjust according to your robot's capabilities

    # Calculate center of the image
    image_center_x = image_width // 2
    image_center_y = image_height // 2

    # Check if the cat is within the safe zone
    if abs(x_center - image_center_x) > safe_zone_width or abs(y_center - image_center_y) > safe_zone_height:
        # Adjust robot movement based on the cat's position relative to the image center
        if x_center < image_center_x:
            left()
        else:
            right()

        if y_center < image_center_y:
            forward()
        else:
            backward()
    else:
        stop()  # Stop the robot if the cat is within the safe zone

def generate_frames():
    while True:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            image_bytes = bytes()
            for chunk in response.iter_content(chunk_size=1024):
                image_bytes += chunk
                a = image_bytes.find(b'\xff\xd8')
                b = image_bytes.find(b'\xff\xd9')
                if a != -1 and b != -1:
                    jpg = image_bytes[a:b + 2]
                    image_bytes = image_bytes[b + 2:]
                    if len(jpg) > 0:
                        nparr = np.frombuffer(jpg, dtype=np.uint8)
                        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                        frame = cv2.resize(frame, (640, 480))
                        (h, w) = frame.shape[:2]
                        imResize = cv2.resize(frame, (300, 300))
                        blob = cv2.dnn.blobFromImage(imResize, 0.007843, (300, 300), 127.5)

                        net.setInput(blob)
                        detections = net.forward()

                        detShape = detections.shape[2]
                        for i in np.arange(0, detShape):
                            confidence = detections[0, 0, i, 2]
                            if confidence > confThresh:
                                idx = int(detections[0, 0, i, 1])
                                if CLASSES[idx] == "cat":
                                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                                    (startX, startY, endX, endY) = box.astype("int")
                                    x_center = (startX + endX) // 2
                                    y_center = (startY + endY) // 2

                                    label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
                                    cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[idx], 2)
                                    if startY - 15 > 15:
                                        y = startY - 15
                                    else:
                                        y = startY + 15
                                    cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

                                    cat_follower_logic(x_center, y_center, w, h)

                        _, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])  # Adjust JPEG quality
                        frame = buffer.tobytes()
                        yield (b'--frame\r\n'
                               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('temp.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    return response

if __name__ == '__main__':
    app.run(debug=True)

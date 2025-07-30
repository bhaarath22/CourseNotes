#frozen file is weights
#ssd is for configration or architecture , most accurate and speed , realtime . this can be used with
# Rasberry phi and jetson non microprocessor/controller
#yolo need GPU so am ignoreing that
# available in openCV Documentation
import cv2
import numpy as np

# Thresholds
conf_threshold = 0.5  # Threshold to detect object
nms_threshold = 0.4

# Initialize webcam
cap = cv2.VideoCapture(0)

# Load class names from coco.names file
classNames = []
classFile = '/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/ObjectDetection/YOLO/coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Load the model using OpenCV's DNN module
model_path = '/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/ObjectDetection/frozen_inference_graph.pb'
config_path = '/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/ObjectDetection/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
net = cv2.dnn.readNetFromTensorflow(model_path, config_path)

# Optional: Set the preferable backend and target for the model
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break

    # Resize image for consistent input size
    img_resized = cv2.resize(img, (320, 320))
    blob = cv2.dnn.blobFromImage(img_resized, 1.0 / 255, (320, 320), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)

    # Perform object detection
    output_layers = net.getUnconnectedOutLayersNames()
    detections = net.forward(output_layers)

    classIds, confs, bbox = [], [], []
    for output in detections:
        for detection in output:
            scores = detection[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > conf_threshold:
                center_x = int(detection[0] * img.shape[1])
                center_y = int(detection[1] * img.shape[0])
                w = int(detection[2] * img.shape[1])
                h = int(detection[3] * img.shape[0])

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                bbox.append([x, y, w, h])
                classIds.append(classId)
                confs.append(float(confidence))

    # Apply Non-Maximum Suppression
    indices = cv2.dnn.NMSBoxes(bbox, confs, conf_threshold, nms_threshold)

    if len(indices) > 0:
        for i in indices.flatten():
            box = bbox[i]
            x, y, w, h = box[0], box[1], box[2], box[3]

            # Draw rectangle around detected object
            cv2.rectangle(img, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)
            cv2.putText(img, f"{classNames[classIds[i]].upper()} {confs[i]:.2f}",
                        (x + 10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the result frame
    cv2.imshow("Object Detection", img)

    # Stop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()

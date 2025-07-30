import cv2
import numpy as np

conf_threshold = 0.5
nms_threshold = 0.4
cap = cv2.VideoCapture(0)

classNames = []
classFile = '/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/ObjectDetection/YOLO/coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

model_path = '/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/ObjectDetection/frozen_inference_graph.pb'
config_path = '/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/ObjectDetection/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'

net = cv2.dnn.readNetFromTensorflow(model_path, config_path)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break

    blob = cv2.dnn.blobFromImage(img, 1.0 / 255, (320, 320), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    detections = net.forward()

    hT, wT, cT = img.shape
    bbox, confs, classIds = [], [], []
    for detection in detections[0, 0, :, :]:
        confidence = detection[2]
        if confidence > conf_threshold:
            x1 = int(detection[3] * wT)
            y1 = int(detection[4] * hT)
            x2 = int(detection[5] * wT)
            y2 = int(detection[6] * hT)
            bbox.append([x1, y1, x2 - x1, y2 - y1])
            confs.append(float(confidence))
            classIds.append(int(detection[1]))

    indices = cv2.dnn.NMSBoxes(bbox, confs, conf_threshold, nms_threshold)
    for i in indices.flatten():
        x, y, w, h = bbox[i]
        label = classNames[classIds[i]] if classIds[i] < len(classNames) else "Unknown"
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, f"{label} {confs[i]:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Object Detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

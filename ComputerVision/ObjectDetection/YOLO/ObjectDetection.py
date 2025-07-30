import cv2
import numpy as np
import os

def load_yolo_weights(weights_path, config_path):
    if not os.path.exists(weights_path):
        print(f"Error: YOLO weights file not found at {weights_path}")
        return None
    if not os.path.exists(config_path):
        print(f"Error: YOLO config file not found at {config_path}")
        return None
    try:
        net = cv2.dnn.readNet(weights_path, config_path)
        return net
    except cv2.error as e:
        print(f"Error loading YOLOv3 weights: {e}")
        return None

def load_class_labels(labels_path):
    if not os.path.exists(labels_path):
        print(f"Error: Class labels file not found at {labels_path}")
        return []
    try:
        with open(labels_path, "r") as f:
            classes = f.read().splitlines()
        return classes
    except Exception as e:
        print(f"Error loading class labels: {e}")
        return []

def detect_objects(net, img, conf_threshold, nms_threshold):
    height, width, _ = img.shape
    blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layer_outputs = net.forward(output_layers_names)

    boxes, confidences, class_ids = [], [], []

    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > conf_threshold:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
    return boxes, confidences, class_ids, indexes

def draw_bounding_boxes(img, boxes, confidences, class_ids, classes, colors, indexes):
    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = f"{confidences[i]:.2f}"
            color = colors[class_ids[i] % len(colors)]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, f"{label} {confidence}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 3)

def main():
    weights_path = '/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/ObjectDetection/YOLO/yolov3.weights'
    config_path = '/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/ObjectDetection/YOLO/yolov3.cfg'
    labels_path = '/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/ObjectDetection/YOLO/coco.names'

    net = load_yolo_weights(weights_path, config_path)
    if net is None:
        return

    classes = load_class_labels(labels_path)
    if not classes:
        return

    # Set this flag to True for webcam, False for image
    use_webcam = True

    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    conf_threshold = 0.5
    nms_threshold = 0.4

    if use_webcam:
        # Webcam handling
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Unable to access the webcam.")
            return

        print("Press 'ESC' to exit.")

        while True:
            ret, img = cap.read()
            if not ret:
                print("Error: Failed to capture frame from webcam.")
                break

            boxes, confidences, class_ids, indexes = detect_objects(net, img, conf_threshold, nms_threshold)
            draw_bounding_boxes(img, boxes, confidences, class_ids, classes, colors, indexes)

            cv2.imshow('YOLOv3 Object Detection', img)

            key = cv2.waitKey(1)
            if key == 27:  # ESC key
                break

        cap.release()
        cv2.destroyAllWindows()

    else:
        # Image handling
        image_path = '/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/Resource/frnds.jpeg'
        img = cv2.imread(image_path)
        if img is None:
            print(f"Error: Unable to load image from path {image_path}")
            return

        boxes, confidences, class_ids, indexes = detect_objects(net, img, conf_threshold, nms_threshold)
        draw_bounding_boxes(img, boxes, confidences, class_ids, classes, colors, indexes)

        # Display the image
        cv2.imshow('YOLOv3 Object Detection', img)
        cv2.waitKey(0)  # Wait for any key press
        cv2.destroyAllWindows()

        # Optional: Save the output image
        output_path = '/ComputerVision/ObjectDetection/YOLO/output_image.jpg'
        cv2.imwrite(output_path, img)
        print(f"Processed image saved at {output_path}")

if __name__ == '__main__':
    main()

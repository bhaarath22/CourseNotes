import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/EmotionRecognition/ERNDA3Emotions/EmotionsDataset/data/angry/0.jpg')

if img is None:
    print("Error: Image not found or could not be loaded.")
else:
    # Convert the image to RGB (OpenCV loads images in BGR by default)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.axis('off')  # Hide axes
    plt.show()

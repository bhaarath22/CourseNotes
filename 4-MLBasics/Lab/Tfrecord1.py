import tensorflow as tf
import cv2
import numpy as np

image_path = "/EmotionRecognition/REALWORLDDAT/WhatsApp Image 2024-12-02 at 09.53.01 (1).jpeg"  # Replace with your image path
image = cv2.imread(image_path)
image = cv2.resize(image, (128, 128))
image_bytes = image.tobytes()


def image_example(image_bytes):
    feature = {
        "image": tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_bytes])),
    }
    return tf.train.Example(features=tf.train.Features(feature=feature)).SerializeToString()

# Writing image to TFRecord
tfrecord_filename = "image.tfrecord"
with tf.io.TFRecordWriter(tfrecord_filename) as writer:
    writer.write(image_example(image_bytes))

print(f"Image saved to {tfrecord_filename}")


 # reading the image from tfrecord
import matplotlib.pyplot as plt

# Defineing feature description for parsing
image_feature_description = {
    "image": tf.io.FixedLenFeature([], tf.string),
}

# Parse function
def parse_image_example(example_proto):
    example = tf.io.parse_single_example(example_proto, image_feature_description)
    image = tf.io.decode_raw(example["image"], tf.uint8)  # Decode raw bytes
    image = tf.reshape(image, (128, 128, 3))  # Reshape to original size
    return image

# Load dataset from TFRecord
dataset = tf.data.TFRecordDataset(tfrecord_filename)
dataset = dataset.map(parse_image_example)

# Read the first image from the dataset
for img in dataset.take(1):
    img = img.numpy()  # Converting tensor to NumPy array

    # Display the image
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.title("Image from TFRecord")
    plt.show()

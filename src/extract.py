import os
import cv2
import numpy as np

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

def preprocess_images(images, target_size=(224, 224)):
    processed_images = [cv2.resize(img, target_size) for img in images]
    return np.array(processed_images)

if __name__ == "__main__":
    folder_path = "data/raw_images"
    images = load_images_from_folder(folder_path)
    processed_images = preprocess_images(images)
    print(f"Loaded {len(processed_images)} images.")

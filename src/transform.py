import numpy as np
import cv2

def apply_augmentation(images):
    augmented_images = []
    for img in images:
        flipped = cv2.flip(img, 1)  # Flip horizontal
        blurred = cv2.GaussianBlur(img, (5, 5), 0)
        augmented_images.extend([img, flipped, blurred])
    return np.array(augmented_images)

if __name__ == "__main__":
    from extract import preprocess_images, load_images_from_folder

    folder_path = "data/raw_images"
    images = load_images_from_folder(folder_path)
    processed_images = preprocess_images(images)
    augmented_images = apply_augmentation(processed_images)

    print(f"Augmented dataset size: {len(augmented_images)} images.")

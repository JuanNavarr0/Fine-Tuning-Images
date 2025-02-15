import tensorflow as tf
import numpy as np

def create_dataset(images, labels):
    dataset = tf.data.Dataset.from_tensor_slices((images, labels))
    dataset = dataset.shuffle(len(images)).batch(32).prefetch(tf.data.experimental.AUTOTUNE)
    return dataset

if __name__ == "__main__":
    from transform import apply_augmentation
    from extract import preprocess_images, load_images_from_folder

    folder_path = "data/raw_images"
    images = load_images_from_folder(folder_path)
    processed_images = preprocess_images(images)
    augmented_images = apply_augmentation(processed_images)

    labels = np.zeros(len(augmented_images))  # Placeholder labels
    dataset = create_dataset(augmented_images, labels)

    print(f"Dataset prepared with {len(augmented_images)} samples.")

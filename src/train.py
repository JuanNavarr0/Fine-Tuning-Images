import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def build_model(input_shape):
    model = keras.Sequential([
        layers.Conv2D(32, (3,3), activation="relu", input_shape=input_shape),
        layers.MaxPooling2D((2,2)),
        layers.Conv2D(64, (3,3), activation="relu"),
        layers.MaxPooling2D((2,2)),
        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dense(10, activation="softmax")  # Para clasificación en 10 clases
    ])
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model

if __name__ == "__main__":
    from load import create_dataset
    import numpy as np

    input_shape = (224, 224, 3)

    # Generamos dataset de prueba
    num_samples = 100
    dummy_images = np.random.rand(num_samples, *input_shape)
    dummy_labels = np.random.randint(0, 10, num_samples)

    dataset = create_dataset(dummy_images, dummy_labels)

    model = build_model(input_shape)
    model.fit(dataset, epochs=5)

    model.save("fine_tuned_model.h5")
    print("Model training complete and saved!")

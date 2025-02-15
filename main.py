from train import build_model
import tensorflow as tf

def load_trained_model(model_path="fine_tuned_model.h5"):
    return tf.keras.models.load_model(model_path)

if __name__ == "__main__":
    model = load_trained_model()
    print("Model loaded successfully.")

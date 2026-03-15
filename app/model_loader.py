# Model loader for sentiment analysis
import pickle
import os

MODEL_PATH = "model/sentimentanalysismodel.pkl"


def load_model():
    print("Loading model...")

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at path: {MODEL_PATH}")

    try:
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
    except Exception as e:
        raise RuntimeError(f"Failed to load model: {e}")

    print("Model loaded successfully.")
    return model
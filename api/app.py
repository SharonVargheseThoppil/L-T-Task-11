
import os
import io
import logging

import numpy as np
import tensorflow as tf

from PIL import Image
from flask import Flask, request, jsonify
from werkzeug.exceptions import RequestEntityTooLarge

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

logging.basicConfig(level=logging.INFO)

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "cifar10_model.keras"
)

CLASS_NAMES = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck"
]

model = None


def load_model():
    global model

    if model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                f"Model not found: {MODEL_PATH}"
            )

        model = tf.keras.models.load_model(
            MODEL_PATH,
            compile=False
        )

        logging.info("Deep learning model loaded.")

    return model


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "application": "CIFAR-10 Deep Learning API",
        "status": "running",
        "endpoints": [
            "/health",
            "/predict"
        ]
    })


@app.route("/health", methods=["GET"])
def health():
    try:
        loaded_model = load_model()

        return jsonify({
            "status": "healthy",
            "model_loaded": loaded_model is not None
        }), 200

    except Exception:
        logging.exception("Health check failed")

        return jsonify({
            "status": "unhealthy",
            "model_loaded": False
        }), 503


@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return jsonify({
            "error": "No image file provided. Use field name 'file'."
        }), 400

    uploaded_file = request.files["file"]

    if uploaded_file.filename == "":
        return jsonify({
            "error": "No file selected."
        }), 400

    try:
        image_bytes = uploaded_file.read()

        image = Image.open(
            io.BytesIO(image_bytes)
        ).convert("RGB")

        image = image.resize((32, 32))

        image_array = np.asarray(
            image,
            dtype=np.float32
        ) / 255.0

        image_array = np.expand_dims(
            image_array,
            axis=0
        )

        loaded_model = load_model()

        predictions = loaded_model.predict(
            image_array,
            verbose=0
        )[0]

        predicted_index = int(np.argmax(predictions))

        return jsonify({
            "predicted_class": CLASS_NAMES[predicted_index],
            "confidence": round(
                float(predictions[predicted_index]) * 100,
                2
            ),
            "probabilities": {
                CLASS_NAMES[i]: round(
                    float(predictions[i]) * 100,
                    2
                )
                for i in range(len(CLASS_NAMES))
            }
        }), 200

    except Exception:
        logging.exception("Prediction failed")

        return jsonify({
            "error": "Unable to process image."
        }), 400


@app.errorhandler(RequestEntityTooLarge)
def handle_large_file(error):
    return jsonify({
        "error": "Image exceeds the 5 MB upload limit."
    }), 413


if __name__ == "__main__":
    load_model()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
import os
import requests
import streamlit as st

from PIL import Image

API_URL = os.getenv(
    "API_URL",
    "http://localhost:5000"
)

st.set_page_config(
    page_title="CIFAR-10 AI Classifier",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 CIFAR-10 Deep Learning Classifier")

st.write(
    "Upload an image to obtain a prediction "
    "from the containerized CNN model."
)

st.info(
    "The classifier recognizes the 10 CIFAR-10 categories. "
    "Predictions for unrelated images may be unreliable."
)

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("Predict Image", type="primary"):

        with st.spinner("Connecting to Flask API..."):

            try:
                uploaded_file.seek(0)

                response = requests.post(
                    f"{API_URL}/predict",
                    files={
                        "file": (
                            uploaded_file.name,
                            uploaded_file.getvalue(),
                            uploaded_file.type
                        )
                    },
                    timeout=120
                )

                response.raise_for_status()

                result = response.json()

                st.success("Prediction completed.")

                st.subheader(
                    f"Predicted Class: {result['predicted_class'].title()}"
                )

                st.metric(
                    "Confidence",
                    f"{result['confidence']:.2f}%"
                )

                st.subheader("Class Probabilities")

                st.bar_chart(
                    result["probabilities"]
                )

            except requests.exceptions.RequestException as error:

                st.error(
                    f"Could not communicate with Flask API: {error}"
                )

            except (KeyError, ValueError) as error:

                st.error(
                    f"Unexpected API response: {error}"
                )

st.divider()

st.caption(
    "Task 11 | Full Application Containerization | "
    "Flask + TensorFlow + Streamlit + Docker"
)
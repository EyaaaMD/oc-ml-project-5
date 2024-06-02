"""
pip install streamlit
"""

import streamlit as st
from joblib import load
import requests

loaded_model = load('models/svc_model.joblib')
loaded_vectorizer = load('models/vectorizer_X.joblib')
multilabel_binarizer = load('models/multilabel_binarizer.joblib')

classes = multilabel_binarizer.classes_

# Streamlit UI
st.title("Questions Multi-label Classification")

input_text = st.text_area("Enter your text here:")

if st.button("Predict (use API)"):
    # Make request to FastAPI app
    response = requests.post("http://localhost:8000/predict/", json={"text": input_text})
    if response.status_code == 200:
        result = response.json()
        predicted_labels = result["predicted_labels"]
        st.success("Predicted labels: {}".format(predicted_labels))
    else:
        st.error("Failed to get predictions. Please try again.")
elif st.button("Predict (locally)"):
    # Make request to FastAPI app
    x = loaded_vectorizer.transform([input_text])
    predictions = loaded_model.predict(x)
    predicted_labels = [classes[i] for i, prediction in enumerate(predictions[0]) if prediction == 1]
    st.success("Predicted labels: {}".format(predicted_labels))
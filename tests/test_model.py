
import pytest
from joblib import load
import numpy as np

# Load the model, vectorizer, and binarizer
model = load('./models/svc_model.joblib')
vectorizer = load('./models/vectorizer_X.joblib')
binarizer = load('./models/multilabel_binarizer.joblib')

classes = binarizer.classes_

@pytest.fixture
def sample_input():
    return "This is a sample input text"

def test_model_loading():
    assert model is not None
    assert vectorizer is not None
    assert binarizer is not None

def test_prediction(sample_input):
    transformed_input = vectorizer.transform([sample_input])
    assert transformed_input.shape[1] == len(vectorizer.get_feature_names_out())

    predictions = model.predict(transformed_input)
    assert predictions.shape[1] == len(classes)
    
    predicted_labels = [classes[i] for i, prediction in enumerate(predictions[0]) if prediction == 1]
    assert isinstance(predicted_labels, list)

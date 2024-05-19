"""
pip install fastapi uvicorn

run: uvicorn app:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load

app = FastAPI()

class InputText(BaseModel):
    text: str

# Load the model and vectorizer
loaded_model = load('model_sgd.joblib')
loaded_vectorizer = load('vectorizer_X.joblib')
multilabel_binarizer = load('multilabel_binarizer.joblib')

classes = multilabel_binarizer.classes_

@app.post("/predict/")
async def predict(input_text: InputText):
    x = loaded_vectorizer.transform([input_text.text])
    predictions = loaded_model.predict(x)
    predicted_labels = [classes[i] for i, prediction in enumerate(predictions[0]) if prediction == 1]
    return {"predicted_labels": predicted_labels}

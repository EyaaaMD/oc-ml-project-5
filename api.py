"""
pip install fastapi uvicorn

run: uvicorn api:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load

app = FastAPI()

class InputText(BaseModel):
    text: str

# Load the model and vectorizer
loaded_model = load('models/svc_model.joblib')
loaded_vectorizer = load('models/vectorizer_X.joblib')
multilabel_binarizer = load('models/multilabel_binarizer.joblib')

classes = multilabel_binarizer.classes_

@app.post("/predict/")
async def predict(input_text: InputText):
    x = loaded_vectorizer.transform([input_text.text])
    predictions = loaded_model.predict(x)
    predicted_labels = [classes[i] for i, prediction in enumerate(predictions[0]) if prediction == 1]
    return {"predicted_labels": predicted_labels}


@app.get("/")
async def hello(input_text: InputText):
    
    return {"message": "Bonjour, depuis ma première app Azure..."}
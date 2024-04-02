from fastapi import FastAPI, HTTPException
from joblib import load
from pydantic import BaseModel

import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.features.text_processing import clean_text

from src.features.text_processing import clean_text

from preprocess import preprocess_input

# Define a Pydantic model for the input data
class InputData(BaseModel):
    content: list  # Assuming each input will be a list of features

app = FastAPI()

vectorizer = load('../models/mh_tfidf_vectorizer.joblib')
model = load('../models/mh_logistic_regression_model.joblib')
@app.post("/predict/")
async def make_prediction(data: InputData):
    try:
        # Here you would need to transform `data.content` into the format your model expects
        # For demonstration, assuming it's already in the correct format
        cleaned_text = [clean_text(text) for text in data.content]
        print(cleaned_text)
        vectorized_text = vectorizer.transform(cleaned_text)
        print(vectorized_text)
        predictions = model.predict(vectorized_text)
        return {"predictions": predictions.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

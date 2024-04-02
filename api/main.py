from fastapi import FastAPI, HTTPException
from joblib import load
from pydantic import BaseModel

import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.features.text_processing import clean_text

from src.features.text_processing import clean_text

from fastapi.middleware.cors import CORSMiddleware


# Define a Pydantic model for the input data
class InputData(BaseModel):
    content: list  # Assuming each input will be a list of features

app = FastAPI()

allowed_origins = [
    "http://localhost:3000",  # Allow frontend running on localhost:3000    
]

# Add CORSMiddleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # Specify the allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

vectorizer = load('../models/mh_tfidf_vectorizer.joblib')
model = load('../models/mh_logistic_regression_model.joblib')



@app.post("/predict/")
async def make_prediction(data: InputData):
    print(data)
    try:
        # Here you would need to transform `data.content` into the format your model expects
        # For demonstration, assuming it's already in the correct format
        cleaned_text = [clean_text(text) for text in data.content]
        print(cleaned_text)
        vectorized_text = vectorizer.transform(cleaned_text)
        custom_messages = []
        predictions = model.predict(vectorized_text)
        for pred in predictions:
            if pred == 0:
                message = "The content provided does not indicate immediate mental health concerns. However, if you're feeling distressed or in need of support, reaching out to a professional can be a valuable step."
            elif pred == 1:
                message = "The content provided suggests possible mental health concerns. It's important to consider speaking with a mental health, you're not alone, and help is available."
            custom_messages.append(message)
        # Return the custom messages
        return {"predictions": custom_messages}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

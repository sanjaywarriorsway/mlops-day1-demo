from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# 1. Load the Model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# 2. Define Input Schema (Data Validation)
class IrisRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(request: IrisRequest):
    # Convert input to array
    data = np.array([[
        request.sepal_length, 
        request.sepal_width, 
        request.petal_length, 
        request.petal_width
    ]])
    
    # Predict
    prediction = model.predict(data)
    
    return {"class": int(prediction[0])}
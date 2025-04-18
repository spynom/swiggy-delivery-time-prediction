from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from data_validation import DataPoint
from load_credentials import load_model
import pandas as pd
import uvicorn


class Data(BaseModel):
    data_points: List[DataPoint]

model = load_model()

app = FastAPI()


# create the home endpoint
@app.get(path="/")
def home():
    return "Welcome to the Swiggy Food Delivery Time Prediction App"

@app.post("/predict")
def predict(data: Data):
    # Convert list of DataPoint to list of dicts
    data_dicts = [dp.model_dump() for dp in data.data_points]

    # Convert to DataFrame
    df = pd.DataFrame(data_dicts)
    try:
        return {"predict":[f"{time_taken:.2f} mins" for time_taken in model.predict(df).tolist()]}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app="app:app",host="0.0.0.0",port=8000)
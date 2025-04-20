from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import BaseModel
from typing import List
from data_validation import DataPoint
from load_credentials import load_model
import pandas as pd
import uvicorn
from prometheus_client import Counter, Histogram, generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST
import time


class Data(BaseModel):
    data_points: List[DataPoint]

model = load_model()


# from prometheus_client import CollectorRegistry

# Create a custom registry
registry = CollectorRegistry()

# Define your custom metrics using this registry
REQUEST_COUNT = Counter(
    "app_request_count", "Total number of requests to the app", ["method", "endpoint"], registry=registry
)
REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds", "Latency of requests in seconds", ["endpoint"], registry=registry
)


app = FastAPI()


# create the home endpoint
@app.get(path="/")
def home():
    return "Welcome to the Swiggy Food Delivery Time Prediction App"

@app.post("/predict")
@app.post("/predict")
def predict(data: Data):
    REQUEST_COUNT.labels(method="POST", endpoint="/predict").inc()
    start_time = time.time()

    try:
        data_dicts = [dp.model_dump() for dp in data.data_points]
        df = pd.DataFrame(data_dicts)
        preds = model.predict(df).tolist()
        return {"predict": [f"{t:.2f} mins" for t in preds]}
    except Exception as e:
        return {"error": str(e)}
    finally:
        REQUEST_LATENCY.labels(endpoint="/predict").observe(time.time() - start_time)


@app.get("/metrics")
def metrics():
    data = generate_latest(registry)
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    uvicorn.run(app="app:app",host="0.0.0.0",port=8000)
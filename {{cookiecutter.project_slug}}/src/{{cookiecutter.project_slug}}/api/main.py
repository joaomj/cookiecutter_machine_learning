# -*- coding: utf-8 -*-
from fastapi import FastAPI

app = FastAPI(
    title="{{ cookiecutter.project_name }} API",
    description="{{ cookiecutter.description }}",
    version="0.1.0" # Or manage version differently
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the {{ cookiecutter.project_name }} API!"}

# TODO: Add prediction endpoints here
# Example:
# from pydantic import BaseModel
# class InputDataModel(BaseModel):
#     feature1: float
#     feature2: int
#
# @app.post("/predict")
# async def predict(data: InputDataModel): # Define InputDataModel using pydantic
#     # Load model, preprocess data, predict, return result
#     # prediction = model.predict([[data.feature1, data.feature2]]) # Example
#     # return {"prediction": prediction.tolist()}
#     return {"message": "Prediction endpoint not implemented yet."}

# Add other endpoints as needed (e.g., health check)
@app.get("/health")
async def health_check():
    return {"status": "ok"}

🏥 Insurance Premium Prediction API (FastAPI + Docker)

This project is a production-ready Machine Learning API that predicts an insurance premium category using a Random Forest classifier.
The ML model is trained offline, serialized using pickle, loaded inside a FastAPI service, and fully containerized using Docker.

The Docker image is published on Docker Hub and can be pulled and run anywhere.

🔗 Docker Hub Repository
https://hub.docker.com/repository/docker/aishikdalui/insurance-premium-prediction

🚀 Key Features
End-to-end ML workflow (training → inference)

Feature engineering & preprocessing pipeline

Random Forest classification model

FastAPI-based REST API

Health check & versioning

Dockerized deployment

Published Docker image

📂 Project Structure

insurance-premium-prediction/
│
├── app.py
│
├── model/
│   ├── model.pkl           # Trained ML pipeline
│   ├── predict.py          # Model loading & prediction logic
│
├── schema/
│   ├── user_input.py       # Input validation schema
│   ├── predection_response.py  # API response schema
│
├── train_model.py          # Model training & serialization
├── insurance.csv           # Training dataset
├── requirements.txt
├── Dockerfile
└── README.md

🧠 Machine Learning Pipeline
1️⃣ Feature Engineering

The raw dataset is enriched with multiple engineered features:

BMI Calculation
bmi = weight / (height ** 2)

Age Group

young (< 25)

adult (25–44)

middle_aged (45–59)

senior (60+)

Lifestyle Risk

Derived from smoking habit and BMI:

high

medium

low

City Tier Encoding

Tier 1 → Metro cities

Tier 2 → Major cities

Tier 3 → Others

2️⃣ Feature Selection

Model Inputs

bmi

age_group

lifestyle_risk

city_tier

income_lpa

occupation

Target

insurance_premium_category

3️⃣ Model Architecture

A Scikit-learn Pipeline is used:

ColumnTransformer

OneHotEncoder for categorical features

Numeric passthrough

RandomForestClassifier

This ensures:

No data leakage

Same preprocessing in training & inference

Clean production deployment

4️⃣ Model Training & Serialization

Train/Test split: 80/20

Algorithm: RandomForestClassifier

Metric: Accuracy

The full pipeline is saved as:

pickle.dump(pipeline, open("model.pkl", "wb"))

🌐 FastAPI Application
API Entry Point (app.py)
from fastapi import FastAPI
from schema.user_input import UserInput
from schema.predection_response import PredictionResponse
from model.predict import predict_output, MODEL_VERSION, model

Available Endpoints
🏠 Home
GET /


Response:

{
  "message": "Insurance Premium Prediction API"
}

❤️ Health Check
GET /health


Response:

{
  "status": "OK",
  "version": "1.0.0",
  "model_loaded": true
}

🔮 Predict Premium Category
POST /predict


Input (JSON):

{
  "bmi": 28.5,
  "age_group": "adult",
  "lifestyle_risk": "medium",
  "city_tier": 1,
  "income_lpa": 12.5,
  "occupation": "private"
}


Output:

{
  "predicted_category": "high"
}

🧩 Schema Validation
UserInput

Handles request validation using Pydantic, ensuring:

Correct data types

Clean API contracts

Safer predictions

PredictionResponse

Standardizes API output format.

🌐 FastAPI Prediction Service

The trained model.pkl is loaded inside FastAPI, exposing a prediction endpoint.

Example Flow
Client Request
   ↓
FastAPI Endpoint
   ↓
model.pkl (Pipeline)
   ↓
Predicted Insurance Premium Category


FastAPI automatically provides:

Interactive Swagger UI

Input validation

High performance async handling

🐳 Dockerization
Dockerfile Highlights
FROM python:3.13.7-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

📦 Docker Hub Deployment
Build Image
docker build -t aishikdalui/insurance-premium-prediction:api .

Run Container
docker run -p 8000:8000 aishikdalui/insurance-premium-prediction:api

API Docs
http://localhost:8000/docs

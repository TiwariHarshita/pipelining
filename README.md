MLOps Pipeline – News Classification

An end-to-end machine learning pipeline for classifying news articles into different categories.

This project demonstrates how to build, train, test, deploy, and monitor a machine learning model using MLOps tools.

The model classifies news articles into four categories:

* World
* Sports
* Business
* Sci/Tech

The project uses the AG News dataset and focuses on making the ML workflow reproducible and easier to maintain.

⸻

1. Project Overview

Training a machine learning model is only one part of an ML project. In a real application, we also need to manage datasets, track experiments, test models, deploy them, and monitor their performance.

This project brings these steps together into one pipeline.

What this project does

Feature	Description
Data ingestion	Downloads and validates the AG News dataset
Data preprocessing	Cleans text and splits data into training, validation, and testing sets
Experiment tracking	Uses MLflow to record experiments and compare models
Data versioning	Uses DVC to track datasets and pipeline changes
Model selection	Selects the best model based on validation accuracy
Model testing	Runs automated tests on data, models, and API endpoints
Model deployment	Serves predictions through a FastAPI application
CI/CD	Uses GitHub Actions to automate testing, training, and Docker builds
Model monitoring	Uses Evidently AI to identify changes in incoming data

⸻

2. Architecture

The project follows a simple workflow:

             AG News Dataset
                    |
                    v
             Data Ingestion
                    |
                    v
             Data Validation
                    |
                    v
             Preprocessing
                    |
                    v
              DVC Versioning
                    |
                    v
             Model Training
                    |
                    v
            MLflow Tracking
                    |
                    v
             Model Evaluation
                    |
                    v
             Model Registry
                    |
                    v
             FastAPI Server
                    |
                    v
             Docker Container
                    |
                    v
              Predictions
                    |
                    v
            Model Monitoring
                    |
                    v
             Drift Detection

GitHub Actions automates the testing, training, and Docker build process whenever changes are pushed to the main branch.

⸻

3. Pipeline Stages

Stage 1: Data Ingestion and Validation

The project downloads the AG News dataset using HuggingFace Datasets.

Before training, the data is checked for:

* Missing columns.
* Null values.
* Class imbalance.
* Duplicate news articles.
* Invalid data formats.

This helps catch data problems before they affect model training.

File: src/ingest.py

Stage 2: Data Preprocessing

The raw news articles are cleaned and prepared for training.

The dataset is divided into three parts:

Dataset	Percentage	Purpose
Training	70%	Used to train the model
Validation	15%	Used to compare models
Testing	15%	Used for final evaluation

A stratified split is used to maintain a similar distribution of news categories in each dataset.

The processed datasets are stored as CSV files and tracked using DVC.

File: src/preprocess.py

Stage 3: Model Training and Experiment Tracking

Three different model configurations are trained and compared.

Experiment	Model	Features
Baseline	Logistic Regression	TF-IDF unigrams
Bigrams	Logistic Regression	TF-IDF unigrams and bigrams
SVM	Calibrated SVM	TF-IDF unigrams and bigrams

MLflow is used to track each experiment.

For every run, the project records:

* Model parameters.
* Accuracy.
* Precision.
* Recall.
* F1-score.
* Model files.
* Confusion matrix.
* Classification report.

This makes it easier to compare experiments and understand which model performs better.

File: src/train.py

Stage 4: Model Selection and Registration

After training, the models are compared using validation accuracy.

The best-performing model is registered in the MLflow Model Registry.

A minimum accuracy threshold of 0.87 is configured.

Only models that pass this threshold are eligible for promotion to Production.

This helps prevent models with poor performance from being deployed.

Stage 5: Automated Testing

Pytest is used to check different parts of the application.

The project contains 71 automated tests.

tests/
├── test_data.py
├── test_model.py
└── test_api.py

The tests cover:

* Data validation and schema checks.
* Training and testing data integrity.
* Model loading and predictions.
* Prediction probability checks.
* API endpoints.
* Invalid and missing inputs.
* Batch predictions.

Stage 6: CI/CD with GitHub Actions

GitHub Actions automates the main pipeline whenever code is pushed to the main branch.

The workflow contains four jobs:

Job 1 – Testing

* Checks code quality.
* Runs automated tests.
* Uses synthetic data for CI testing.

Job 2 – Training and Evaluation

* Runs data ingestion and preprocessing.
* Trains the three model configurations.
* Evaluates model performance.
* Checks whether the accuracy threshold is met.

Job 3 – Docker Build

* Builds the Docker image.
* Pushes the image to DockerHub.
* Runs a Trivy security scan.

Job 4 – Pipeline Summary

* Collects the results of previous jobs.
* Displays the pipeline status and model metrics in GitHub Actions.

This reduces the need to manually run every step after making code changes.

Workflow: .github/workflows/ci.yml

Stage 7: Model Serving with FastAPI

The trained model is made available through a REST API built using FastAPI.

The API provides four main endpoints.

Endpoint	Method	Purpose
/predict	POST	Classifies a single news article
/predict/batch	POST	Classifies multiple articles
/model/info	GET	Returns model version and metrics
/health	GET	Checks whether the API and model are running

The API also returns prediction confidence scores and model information.

The application loads the Production model from MLflow and has a local model fallback if the tracking server is unavailable.

Stage 8: Model Monitoring and Drift Detection

A model may perform differently over time when the incoming data changes.

To monitor this, the project uses Evidently AI.

It compares incoming data with the original training data and checks for changes in:

* Text length.
* Word count.
* Average word length.
* Number of sentences.
* Uppercase character ratio.
* Digit ratio.

Population Stability Index (PSI) is used to measure changes in feature distributions.

An HTML report is generated to help understand the detected changes.

File: monitoring/monitor.py

⸻

4. Project Structure

mlops-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── ingest.py
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── serve.py
│
├── tests/
│   ├── test_data.py
│   ├── test_model.py
│   └── test_api.py
│
├── monitoring/
│   └── monitor.py
│
├── models/
├── reports/
├── mlruns/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── docker-compose.yml
├── dvc.yaml
├── params.yaml
├── requirements.txt
└── README.md

⸻

5. Tech Stack

Technology	How it is used
Python	Main programming language
Scikit-learn	Text classification models
HuggingFace Datasets	Downloading AG News
DVC	Dataset versioning and pipeline management
MLflow	Experiment tracking and model registry
FastAPI	Creating the prediction API
Pytest	Automated testing
Docker	Packaging the application
GitHub Actions	CI/CD automation
Evidently AI	Data drift monitoring
DockerHub	Storing Docker images

⸻

6. Getting Started

Requirements

Make sure you have the following installed:

* Python 3.10 or later.
* Git.
* Docker.
* DVC.

Step 1: Clone the repository

git clone YOUR_REPOSITORY_URL
cd mlops-pipeline

Step 2: Create a virtual environment

python -m venv venv

Activate it:

macOS/Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate

Step 3: Install dependencies

pip install -r requirements.txt

Step 4: Initialise DVC

dvc init

If the dataset is already available locally, track it using:

dvc add data/raw

Step 5: Start the MLflow tracking server

mlflow server \
  --host 127.0.0.1 \
  --port 5001 \
  --backend-store-uri sqlite:///mlruns/mlflow.db \
  --default-artifact-root ./mlruns/artifacts

Open the MLflow dashboard at:

http://localhost:5001

Step 6: Run the pipeline

Run individual stages:

python src/ingest.py
python src/preprocess.py
python src/train.py
python src/evaluate.py

Or execute the complete DVC pipeline:

dvc repro

Step 7: Run automated tests

pytest tests/ -v

Step 8: Start the API

uvicorn src.serve:app --host 127.0.0.1 --port 8000 --reload

API documentation:

http://localhost:8000/docs

Step 9: Generate a drift report

python monitoring/monitor.py

The report is generated at:

reports/drift_report.html

⸻

7. API Usage

Single Prediction

Request:

curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Apple stock rose after strong quarterly earnings.",
    "top_k": 3
  }'

Example response:

{
  "label": "Business",
  "label_id": 2,
  "confidence": 0.91,
  "model_version": "3",
  "latency_ms": 8.4
}

Batch Prediction

The batch endpoint allows multiple news articles to be classified in one request.

curl -X POST http://localhost:8000/predict/batch \
  -H "Content-Type: application/json" \
  -d '{
    "texts": [
      "The stock market increased today.",
      "Manchester City won the football match."
    ]
  }'

⸻

8. Model Results

The project compares three model configurations using validation accuracy and F1-score.

Experiment Comparison

Model	Validation Accuracy	Validation F1
Logistic Regression (Unigrams)	88.61%	88.53%
Logistic Regression (Bigrams)	88.91%	88.85%
Calibrated SVM (Bigrams)	89.03%	88.98%

Final Test Results

Metric	Score
Test Accuracy	87.88%
Macro F1-score	87.85%
AUC-ROC	97.29%

These results are based on the project’s reported evaluation runs. Running the pipeline with a different dataset version or configuration may produce different results.

⸻

9. Docker Usage

The application can also be run using Docker.

Pull the image:

docker pull YOUR_DOCKERHUB_USERNAME/mlops-news-classifier:latest

Run the API:

docker run -p 8000:8000 \
  YOUR_DOCKERHUB_USERNAME/mlops-news-classifier:latest

To start the local services using Docker Compose:

docker-compose up

⸻

10. Future Improvements

Some improvements planned for the project include:

* Add Prometheus metrics for API monitoring.
* Create Grafana dashboards for model performance.
* Add support for transformer-based models such as DistilBERT.
* Configure remote DVC storage using AWS S3.
* Deploy the application to Kubernetes.
* Add automated model retraining when significant drift is detected.
* Implement model rollback when a newly deployed model fails evaluation checks.

⸻

Author

Harshita Tiwari

GitHub: Harshita Tiwari

⸻

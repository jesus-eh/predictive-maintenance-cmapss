# Predictive Maintenance using NASA C-MAPSS

This project focuses on predicting the Remaining Useful Life (RUL) of aircraft engines using the NASA C-MAPSS dataset.  
The goal is to build an end-to-end machine learning pipeline for predictive maintenance.

## Problem Description
Predictive maintenance aims to anticipate equipment failures before they occur.  
In this project, we estimate the RUL (number of cycles before failure) of turbofan engines based on multivariate sensor data.

## Dataset
The dataset used is NASA C-MAPSS FD001, which contains:
- 100 engines
- Multiple operational cycles per engine
- 21 sensor measurements per cycle

Each engine runs until failure, and the task is to predict how many cycles remain.

## Project Structure

predictive-maintenance-cmapss/
│
├── data/ # Raw dataset
├── notebooks/ # EDA and experiments
├── src/ # Reusable ML pipeline
├── models/ # Trained models
├── app/ # Inference application


## Pipeline
1. Exploratory Data Analysis (EDA)
2. Feature Engineering
3. Model Training
4. Model Evaluation
5. Inference API

## Model
- Algorithm: Random Forest Regressor
- Input: Engine sensor features
- Output: Remaining Useful Life (RUL)

## Results (FD001)
- MAE: 24.18 cycles  
- RMSE: 34.38 cycles  

## Technologies
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Joblib / Pickle

## How to Run
1. Clone the repository
2. Install dependencies
3. Run the notebooks in order
4. Use app.py for inference

## Future Work
- Try advanced models (XGBoost, LSTM)
- Hyperparameter tuning
- Cross-validation
- Deployment with FastAPI or Docker

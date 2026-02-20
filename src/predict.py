import joblib
import pandas as pd

def predict(input_df: pd.DataFrame, model_path: str = 'models/best.joblib'):
    model = joblib.load(model_path)
    return model.predict(input_df)
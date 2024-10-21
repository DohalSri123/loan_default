import joblib
import os

# Path to the model file
MODEL_PATH = r'C:\Users\knsak\Desktop\loan_default_prediction\export.pkl'

# Load the Random Forest model
model = joblib.load(MODEL_PATH)

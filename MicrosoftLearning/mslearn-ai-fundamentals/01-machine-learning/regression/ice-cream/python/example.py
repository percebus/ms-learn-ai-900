import joblib
import pandas as pd
import numpy as np

# Load the downloaded model
model = joblib.load('unique-job-name-child1-1_model.pkl')

# Prepare sample data (replace with your actual feature values)
sample_data = {
    'DayOfWeek': 'Tuesday',
    'Month': 'April',
    'Temperature': 59.4,
    'Rainfall': 0.74
}

# Convert to DataFrame
df = pd.DataFrame(sample_data)

# Make prediction
prediction = model.predict(df)
print(f"Prediction: {prediction[0]}")

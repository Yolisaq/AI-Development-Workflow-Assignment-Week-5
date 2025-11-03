# preprocessing.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data():
    # Create synthetic hospital dataset
    np.random.seed(42)
    data = pd.DataFrame({
        'age': np.random.randint(20, 90, 1000),
        'num_prev_admissions': np.random.randint(0, 6, 1000),
        'length_of_stay': np.random.randint(1, 15, 1000),
        'chronic_conditions': np.random.randint(0, 3, 1000),
        'lab_result_score': np.random.normal(100, 15, 1000),
        'readmitted': np.random.choice([0, 1], 1000, p=[0.8, 0.2])
    })
    data.to_csv('data/synthetic_patient_data.csv', index=False)
    return data

def preprocess_data(df):
    X = df.drop('readmitted', axis=1)
    y = df['readmitted']

    # Scale numerical features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test, scaler

if __name__ == "__main__":
    df = load_data()
    X_train, X_test, y_train, y_test, scaler = preprocess_data(df)
    print("✅ Data preprocessing complete.")

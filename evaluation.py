# evaluation.py
import joblib
import pandas as pd
from sklearn.metrics import classification_report, roc_auc_score
from preprocessing import preprocess_data

def evaluate_model():
    model = joblib.load('model.joblib')
    df = pd.read_csv('data/synthetic_patient_data.csv')

    X_train, X_test, y_train, y_test, scaler = preprocess_data(df)
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    print("\n📊 Classification Report:")
    print(classification_report(y_test, y_pred))
    print(f"ROC-AUC Score: {roc_auc_score(y_test, y_proba):.2f}")

if __name__ == "__main__":
    evaluate_model()

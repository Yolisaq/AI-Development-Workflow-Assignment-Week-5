# model.py
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score
import joblib
from preprocessing import load_data, preprocess_data

def train_model():
    df = load_data()
    X_train, X_test, y_train, y_test, scaler = preprocess_data(df)

    # Initialize model
    model = LogisticRegression(max_iter=1000, penalty='l2')

    # Train
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    print("Confusion Matrix:\n", cm)
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

    # Save model and scaler
    joblib.dump(model, 'model.joblib')
    joblib.dump(scaler, 'scaler.joblib')
    print("✅ Model and scaler saved successfully.")

if __name__ == "__main__":
    train_model()

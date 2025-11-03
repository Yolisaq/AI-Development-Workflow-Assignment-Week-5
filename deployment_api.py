# deployment_api.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load('model.joblib')
scaler = joblib.load('scaler.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Expect input as JSON list of feature values
    features = np.array(data['features']).reshape(1, -1)
    scaled_features = scaler.transform(features)
    prediction = model.predict(scaled_features)[0]
    probability = model.predict_proba(scaled_features)[0, 1]

    response = {
        'readmission_prediction': int(prediction),
        'probability': round(float(probability), 2)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

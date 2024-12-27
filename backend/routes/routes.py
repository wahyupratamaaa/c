from flask_restful import Resource, reqparse
import joblib
import os
import numpy as np

# Load your trained model
MODEL_DIR = os.path.dirname(os.path.abspath(__file__))  # Mendapatkan direktori file saat ini
MODEL_PATH = os.path.join(MODEL_DIR, "../HeartDisease_Model.pkl")  # Path ke file model

# Load model menggunakan joblib
model = joblib.load(MODEL_PATH)

# Resource class for prediction
class ModelPredict(Resource):
    def post(self):  # Method POST
        # Parse JSON input
        parser = reqparse.RequestParser()
        parser.add_argument("age", type=float, required=True, help="Age is required")
        parser.add_argument("sex", type=int, required=True, help="Sex is required")
        parser.add_argument("cp", type=int, required=True, help="Chest pain type is required")
        parser.add_argument("trestbps", type=float, required=True, help="Resting BP is required")
        parser.add_argument("chol", type=float, required=True, help="Cholesterol level is required")
        parser.add_argument("fbs", type=int, required=True, help="Fasting blood sugar is required")
        parser.add_argument("restecg", type=int, required=True, help="Rest ECG is required")
        parser.add_argument("thalach", type=float, required=True, help="Max HR is required")
        parser.add_argument("exang", type=int, required=True, help="Exercise-induced angina is required")
        parser.add_argument("oldpeak", type=float, required=True, help="Oldpeak is required")
        parser.add_argument("slope", type=int, required=True, help="Slope is required")
        parser.add_argument("ca", type=int, required=True, help="CA is required")
        parser.add_argument("thal", type=int, required=True, help="Thalassemia is required")
        
        args = parser.parse_args()  # Parse input

        # Extract features and reshape them for the model
        features = [
            args["age"], args["sex"], args["cp"], args["trestbps"], args["chol"],
            args["fbs"], args["restecg"], args["thalach"], args["exang"],
            args["oldpeak"], args["slope"], args["ca"], args["thal"]
        ]
        input_array = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_array)[0]  # Binary output: 0 or 1

        # Map prediction to a human-readable output and suggestion
        if prediction == 1:
            result = "Heart Disease Detected"
            suggestion = "We recommend consulting a doctor for further evaluation."
        else:
            result = "No Heart Disease Detected"
            suggestion = "Your results suggest a low risk of heart disease. Continue maintaining a healthy lifestyle, but it is always good to consult a doctor for regular check-ups."

        # Response data
        response = {
            "prediction": result,
            "suggestion": suggestion
        }

        return response, 200  # 200 status code for success

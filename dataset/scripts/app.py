from flask import Flask, request, jsonify
import joblib
import os
 
app = Flask(__name__)
 
# Path to the trained model
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "models"))
model_path = os.path.join(BASE_DIR, "model.pkl")
 
# Load the pipeline
model = joblib.load(model_path)
 
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("transaction", "")
 
    # Use the pipeline for prediction
    prediction = model.predict([text])[0]
    confidence = max(model.predict_proba([text])[0])
 
    return jsonify({
        "transaction": text,
        "predicted_category": prediction,
        "confidence": round(float(confidence), 4)
    })
 
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

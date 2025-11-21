from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("transaction", "")

    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]
    confidence = max(model.predict_proba(vector)[0])

    return jsonify({
        "transaction": text,
        "predicted_category": prediction,
        "confidence": round(float(confidence), 4)
    })

if __name__ == "__main__":
    app.run(debug=True)

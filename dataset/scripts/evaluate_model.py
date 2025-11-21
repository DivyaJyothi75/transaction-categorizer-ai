import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix
import json

# Load data
df = pd.read_csv("../dataset/transactions.csv")
X = df["transaction"]
y = df["category"]

# Load model
model = joblib.load("../models/model.pkl")

# Predict
preds = model.predict(X)

# Generate metrics
report = classification_report(y, preds, output_dict=True)
conf_matrix = confusion_matrix(y, preds)

# Save results
results = {
    "macro_f1": report["macro avg"]["f1-score"],
    "per_class_f1": {cls: report[cls]["f1-score"] for cls in report if cls not in ["accuracy", "macro avg", "weighted avg"]},
    "confusion_matrix": conf_matrix.tolist()
}

with open("../models/evaluation.json", "w") as f:
    json.dump(results, f, indent=4)

print("Evaluation complete! Results saved to models/evaluation.json")
print(json.dumps(results, indent=4))

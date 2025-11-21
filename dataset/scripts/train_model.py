import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os

# Load dataset
df = pd.read_csv("../dataset/transactions.csv")

X = df["transaction"]
y = df["category"]

# Build ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=200))
])

# Train
model.fit(X, y)

# Create models directory if not exists
os.makedirs("../models", exist_ok=True)

# Save model
joblib.dump(model, "../models/model.pkl")

print("Model training complete! Saved model to models/model.pkl")

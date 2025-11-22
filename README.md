curl -X POST http://<EC2_PUBLIC_IP>:5000/predict \
-H "Content-Type: application/json" \
-d '{"transaction": "Bought groceries for $50"}'

{
  "transaction": "Bought groceries for $50",
  "predicted_category": "Shopping",
  "confidence": 0.1945
}

Transaction Categorizer AI – Hackathon Project
 
Overview
 
Transaction Categorizer AI is an ML-powered financial classification system that reads a user’s transaction text and automatically predicts its category such as Food, Shopping, Travel, Groceries, Utilities, etc.
This project is built as part of the Hackathon Round-2 submission to demonstrate real-world application of ML + Flask + Cloud deployment.
 

 
Project Structure
 
transaction-categorizer-ai/
│
├── dataset/
│   ├── data.csv              ← Training data
│   ├── scripts/
│       ├── train_model.py    ← Model training script
│       ├── evaluate_model.py ← Model evaluation script
│       ├── app.py            ← Flask API
│       ├── flask.log         ← Flask logs
│
├── model.pkl                 ← Saved ML model
├── vectorizer.pkl            ← Saved vectorizer
├── README.md                 ← Documentation
├── venv/                     ← Virtual environment
 
 
 
Features
 
✔ ML classification of transactions
✔ NLP preprocessing
✔ REST API built using Flask
✔ Deployed on AWS EC2
✔ Accessible using CURL/Postman
✔ Lightweight, fast, and scalable
 

 
Training the Model
 
Run:
 
cd dataset/scripts
python3 train_model.py
 
This generates:
 
model.pkl
vectorizer.pkl
 

 
Starting the Flask API
 
source venv/bin/activate
cd dataset/scripts
python3 app.py
 
API runs on:
 
http://0.0.0.0:5000
 

 
API Endpoint
 
POST /predict
 
Request:
 
{
  "transaction": "Bought groceries for $50"
}
 
Curl:
 
curl -X POST http://<EC2_PUBLIC_IP>:5000/predict \
-H "Content-Type: application/json" \
-d '{"transaction": "Bought groceries for $50"}'
 
Response:
 
{
  "transaction": "Bought groceries for $50",
  "predicted_category": "Shopping",
  "confidence": 0.1945
}
 

 
Deployment on AWS EC2
 
Steps
 
1. Launch EC2 (Amazon Linux 2023)
 
 
2. Install Python & Git
 
 
3. Clone repo
 
 
4. Setup virtual environment
 
 
5. Install dependencies
 
 
6. Run Flask app
 
 
7. Allow port 5000 in security group
 
 
8. Test API from any device
 

 
Real-World Application
 
This project can be integrated into:
 
Banking / Financial apps
 
Expense tracking apps
 
Automated accounting systems
 
Personal budget management tools


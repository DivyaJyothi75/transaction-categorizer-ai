from flask import Flask,request, jsonify
app= Flask(__name___)

@app.route("/")
def home():
  return"Transaction Categorization AI App is running!"

if__name__== "__main__": app.run(debug=True)

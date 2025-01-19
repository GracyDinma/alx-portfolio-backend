import json
from flask import Flask, request, jsonify
from flask import render_template
from flask_cors import CORS
import requests
from transformers import BertForSequenceClassification, BertTokenizer
import torch
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from services.nlp_service import predict_question
from pymongo import MongoClient
from datetime import datetime



# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['chatbot_db']
collection = db['faq_questions']

# 


app = Flask(__name__)
#CORS(app)

# Fonction pour insérer dans la base de données
def insert_question_to_db(question_id, question, answer, category):
    question_data = {
            "id": question_id,
        "question": question,
        "answer": answer,
        "category": category,
        "date": datetime.now()
    } 
    collection.insert_one(question_data)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/check_nlp_connection', methods=['GET'])
def check_nlp_connection():
    try:
        # Simulating a connection check to the NLP engine
        response = requests.get('http://your-nlp-engine-url/status')  # Adjust the URL for your NLP engine status check
        if response.status_code == 200:
            return jsonify({"status": "connected"}), 200
        else:
            return jsonify({"status": "disconnected"}), 503
    except Exception as e:
        return jsonify({"status": "disconnected", "error": str(e)}), 503
        

@app.route('/ask', methods=['POST'])
def ask():

    # Receive a question on JSON format
    data = request.get_json()  
    question = data.get("question")

    if not question:
        return jsonify({'error': 'No question provided'}), 400

    # Predict answer
    question_id, answer, category = predict_question(question)


    # Insert in Mongo
    insert_question_to_db(question_id, question, answer, category)

    return jsonify({'question_id': question_id, 'question': question, 'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)

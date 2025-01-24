# **SmartConnect Chatbot**

SmartConnect is an AI-powered chatbot designed to handle business FAQs dynamically and provide personalized responses. Built with Flask, it integrates a custom RESTful API with NLP capabilities using NLTK. The app ensures seamless interaction between the frontend, backend, and database, making it scalable and efficient.

---

## **Features**
- Dynamic FAQ management with CRUD operations.
- AI-powered intent recognition and response generation.
- RESTful API for smooth interaction with the frontend.
- MongoDB for efficient data storage and retrieval.

 [read more on the documentation](https://docs.google.com/document/d/1ikLInK_oUlSFGLW0aa5A6KSZncqqfJe1EzR2aomcG7E/edit?usp=sharing)
---

## **Prerequisites**
Before you begin, ensure you have the following installed:
- **Python**: Version 3.8 or higher
- **pip**: Python package manager
- **MongoDB**: Local or cloud setup
- **Git**: Version control system
- **Requirement file**: requirement.txt
---

## **Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/GracyDinma/alx-portfolio-backend.git
   cd alx-portfolio-backend
2. **Set up a virtual environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Linux/Mac
    venv\Scripts\activate      # On Windows
3. **Install dependencies**
     ```bash
     pip install -r requirements.txt
4. **Connections**
    gunicorn--workers=4--threads=2 routes:app
     
5. **Run the application**
    ```bash
    python run.py
6. **Access the app**
Open your browser and visit
  ```bash
   http://127.0.0.1:8000
  


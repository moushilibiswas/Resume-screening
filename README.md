# Resume-screening
File Description

login.py
Acts as the main dashboard (CV Pro).

Sidebar navigation (Home, Resume Builder, Resume Screening)

Chatbot-style interaction on the Home page

Launches the resume screening app

main.py
Core resume screening application.

Handles resume upload

Extracts text from PDFs

Detects language and validates CV

Applies TF-IDF + ML classifier

Predicts job category

Resume_Screening_with_Python.ipynb
Jupyter Notebook used for:

Data preprocessing

Model training

Feature extraction

Experimentation and evaluation

clf.pkl
Trained classification model (pickle file)

tfidf.pkl
Trained TF-IDF vectorizer (pickle file)

🧠 Machine Learning Pipeline

Resume text extraction (PDF/TXT)

Text cleaning (regex-based)

TF-IDF vectorization

Classification using a trained ML model

Mapping prediction IDs to job roles

🛠️ Tech Stack

Python

Streamlit

Scikit-learn

NLTK

PyPDF2

LangDetect

Pickle

▶️ How to Run the Project
1. Install Dependencies
pip install streamlit nltk scikit-learn PyPDF2 langdetect googletrans==4.0.0-rc1

2. Run the Application
streamlit run login.py

📌 Notes

Ensure clf.pkl and tfidf.pkl are present in the root directory.

Internet connection is required on first run for NLTK downloads.

Resume language validation helps filter fake or invalid files.

📊 Output Example

Predicted Category: Data Science

Invalid File: Not a CV

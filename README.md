# Resume-screening

## 🧠 Machine Learning Workflow

1. Resume upload (PDF/TXT)
2. Text extraction
3. Resume cleaning using Regex & NLP
4. Feature extraction using TF-IDF
5. Resume classification using trained ML model
6. Job role prediction

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- NLTK
- PyPDF2
- LangDetect
- Pickle

---

## ▶️ Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/resume-screening-app.git
cd resume-screening-app
2️⃣ Install Dependencies
bash
Copy code
pip install streamlit nltk scikit-learn PyPDF2 langdetect googletrans==4.0.0-rc1
3️⃣ Run the Application
bash
Copy code
streamlit run login.py
📊 Sample Output
Predicted Category: Data Science

Invalid File: Not a CV

📌 Important Notes
Ensure clf.pkl and tfidf.pkl are present in the root directory.

First-time execution downloads NLTK datasets.

Language validation helps filter fake or invalid resumes.

🚀 Future Enhancements
Resume ranking system

Skill extraction

Recruiter dashboard

Database integration

Multi-language resume support

👤 Author
Mpushili Biswas
Resume Screening System using Machine Learning

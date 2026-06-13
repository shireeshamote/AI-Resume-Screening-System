# 🤖 AI Resume Screening System

## 📌 Overview

AI Resume Screening System is a machine learning-based application that helps recruiters analyze and rank resumes efficiently. The system extracts candidate information from PDF resumes, compares it with a job description, calculates a match score, and ranks candidates based on their suitability.

## 🚀 Features

* Upload multiple PDF resumes
* Extract candidate skills automatically
* Identify experience and education details
* Compare resumes with job descriptions
* Calculate ATS-style match scores
* Rank candidates based on relevance
* Download screening results as CSV
* Interactive dashboard built with Streamlit

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* PDFPlumber
* Scikit-learn
* TF-IDF Vectorization
* Cosine Similarity

## 📂 Project Structure

AI-Resume-Screening-System/

├── app.py

├── requirements.txt

├── README.md

└── sample_resumes/

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/AI-Resume-Screening-System.git
```

2. Navigate to the project folder

```bash
cd AI-Resume-Screening-System
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
streamlit run app.py
```

## 📊 How It Works

1. Enter the job description.
2. Upload one or more PDF resumes.
3. Click **Analyze Resumes**.
4. The system extracts skills, experience, and education.
5. Match scores are calculated using TF-IDF and Cosine Similarity.
6. Candidates are ranked and displayed.
7. Download the results as a CSV file.

## 🎯 Future Enhancements

* Advanced NLP-based skill extraction
* AI-powered candidate recommendations
* Interview question generation
* Resume improvement suggestions
* Integration with job portals

## 👩‍💻 Author
Mote Shireesha
B.Tech (CSE - AIML)
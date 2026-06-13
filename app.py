import streamlit as st
import pdfplumber
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

skills_db = [
    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "data analysis",
    "data science",
    "nlp",
    "power bi",
    "excel",
    "aws",
    "azure",
    "cloud computing",
    "html",
    "css",
    "javascript",
    "react",
    "django",
    "flask",
    "git"
]

def extract_skills(text):
    text = text.lower()

    found_skills = []
    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return found_skills

import re

def extract_experience(text):

    pattern = r'(\d+)\s*(year|years)'

    matches = re.findall(
        pattern,
        text.lower()
    )

    if matches:
        return matches[0][0] + " Years"

    return "Not Mentioned"


def extract_education(text):

    education_keywords = [
        "b.tech",
        "btech",
        "m.tech",
        "mtech",
        "b.e",
        "be",
        "mba",
        "bsc",
        "msc",
        "degree"
    ]
    
    text = text.lower()

    for edu in education_keywords:

        if edu in text:
            return edu.upper()

    return "Not Found"

st.set_page_config(page_title="AI Resume Screening System")

st.title("🤖 AI Resume Screening System")

st.subheader("📝 Enter Job Description")
job_description = st.text_area("Enter Job Description")

# 👇 ADD THIS PART HERE
st.subheader("📤 Upload Resumes")

uploaded_files = st.file_uploader(
    "Drag & drop your PDF resumes here or click to browse",
    type=["pdf"],
    accept_multiple_files=True,
    help="Upload multiple resumes in PDF format for analysis"
)

# Then your button comes next
if st.button("Analyze Resumes"):

    if job_description and uploaded_files:

        results = []

        for file in uploaded_files:

            text = ""

            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

            skills = extract_skills(text)
            experience = extract_experience(text)
            education = extract_education(text)

            documents = [job_description, text]

            vectorizer = TfidfVectorizer(
                stop_words="english"
            )

            tfidf_matrix = vectorizer.fit_transform(
                documents
            )

            score = cosine_similarity(
                tfidf_matrix[0:1],
                tfidf_matrix[1:2]
            )[0][0] * 100

            if score >= 75:
                status = "Shortlisted"
            elif score >= 30:
                status = "Consider"
            else:
                status = "Rejected"

            results.append([
                file.name,
                round(score, 2),
                ", ".join(skills),
                 experience,
                education,
                status
            ])

        df = pd.DataFrame(
            results,
            columns=[
                "Resume",
                "Match Score (%)",
                "Skills Found",
                "Experience",
                "Education",
                "Status"
            ]
        )

        df = df.sort_values(
            by="Match Score (%)",
            ascending=False
        )

        st.subheader("Candidate Rankings")

        st.dataframe(df)

        st.bar_chart(
            df.set_index("Resume")[
                "Match Score (%)"
            ]
        )

        csv = df.to_csv(index=False)

        st.download_button(
            label="Download Results CSV",
            data=csv,
            file_name="resume_ranking.csv",
            mime="text/csv"
        )
    else:
        st.warning(
            "Please enter Job Description and upload resumes."
        )
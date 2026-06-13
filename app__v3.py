import streamlit as st
import pdfplumber
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Resume Screening System")

st.title("🤖 AI Resume Screening System")

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

job_description = st.text_area(
    "Enter Job Description"
)

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

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

            if score >= 30:
                status = "Shortlisted"
            elif score >= 15:
                status = "Consider"
            else:
                status = "Rejected"

            results.append([
                file.name,
                round(score, 2),
                ", ".join(skills),
                status
            ])

        df = pd.DataFrame(
            results,
            columns=[
                "Resume",
                "Match Score (%)",
                "Skills Found",
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
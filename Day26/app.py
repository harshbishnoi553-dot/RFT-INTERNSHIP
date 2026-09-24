import streamlit as st
import pandas as pd
import re

st.set_page_config(
    page_title="AI Resume Screening Tool",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Screening Tool")
st.write("Upload resumes and compare them with a job description.")

job_description = st.text_area(
    "📋 Enter Job Description",
    "We are looking for a Python developer with Python, SQL, Pandas, Machine Learning, Git and GitHub skills."
)

uploaded_files = st.file_uploader(
    "📄 Upload Resume Files",
    type=["txt", "csv"],
    accept_multiple_files=True
)

skills_list = [
    "Python",
    "Java",
    "C++",
    "SQL",
    "Excel",
    "Pandas",
    "NumPy",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "Power BI",
    "Tableau",
    "Git",
    "GitHub",
    "Django",
    "Flask",
    "AWS",
    "Docker",
    "HTML",
    "CSS",
    "JavaScript",
    "React"
]

def extract_name(text):
    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if line:
            return line

    return "Unknown"


def extract_skills(text):
    found_skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


def extract_experience(text):
    pattern = r"(\d+)\+?\s*(?:years|year)"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group(1) + " years"

    return "Not Found"


def extract_education(text):
    education_list = [
        "B.Tech",
        "B.E",
        "BCA",
        "MCA",
        "M.Tech",
        "MBA",
        "B.Sc",
        "M.Sc",
        "Bachelor",
        "Master",
        "Engineering",
        "Computer Science"
    ]

    found = []

    for education in education_list:
        if education.lower() in text.lower():
            found.append(education)

    if found:
        return ", ".join(found)

    return "Not Found"


def calculate_score(resume_skills, job_skills):
    if len(job_skills) == 0:
        return 0

    matched_skills = set(resume_skills) & set(job_skills)

    score = (len(matched_skills) / len(set(job_skills))) * 100

    return round(score, 2)


if uploaded_files:

    job_skills = extract_skills(job_description)

    results = []

    for file in uploaded_files:

        if file.name.endswith(".txt"):

            text = file.read().decode(
                "utf-8",
                errors="ignore"
            )

        elif file.name.endswith(".csv"):

            df = pd.read_csv(file)

            text = " ".join(
                df.astype(str)
                .fillna("")
                .values
                .flatten()
            )

        resume_skills = extract_skills(text)

        missing_skills = list(
            set(job_skills) - set(resume_skills)
        )

        score = calculate_score(
            resume_skills,
            job_skills
        )

        results.append({
            "Name": extract_name(text),
            "Resume": file.name,
            "Skills": ", ".join(resume_skills),
            "Experience": extract_experience(text),
            "Education": extract_education(text),
            "Match Score": score,
            "Missing Skills": ", ".join(missing_skills)
        })

    result_df = pd.DataFrame(results)

    result_df = result_df.sort_values(
        by="Match Score",
        ascending=False
    )

    st.subheader("🏆 Candidate Ranking")

    st.dataframe(
        result_df,
        use_container_width=True
    )

    st.subheader("📊 Resume Match Score")

    chart_data = result_df.set_index(
        "Name"
    )["Match Score"]

    st.bar_chart(chart_data)

    st.subheader("🎯 Shortlisting")

    threshold = st.slider(
        "Select Minimum Match Score",
        0,
        100,
        50
    )

    shortlisted = result_df[
        result_df["Match Score"] >= threshold
    ]

    st.write(
        f"Candidates with score ≥ {threshold}%"
    )

    st.dataframe(
        shortlisted,
        use_container_width=True
    )

    csv_file = shortlisted.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download Shortlisted Candidates",
        data=csv_file,
        file_name="shortlisted_candidates.csv",
        mime="text/csv"
    )

else:

    st.info(
        "👆 Upload one or more resume files to start screening."
    )
import streamlit as st
import plotly.graph_objects as go

from utils.resume_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.job_matcher import match_jobs

st.set_page_config(
    page_title="AI Career Intelligence Copilot",
    layout="wide"
)

st.title("🚀 AI Career Intelligence Copilot")
st.write("Upload your resume PDF and get career insights.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    # Resume Text
    text = extract_text_from_pdf(uploaded_file)

    st.subheader("📄 Resume Preview")

    st.text_area(
        "Resume Text",
        text[:3000],
        height=250
    )

    # Skills
    skills = extract_skills(text)

    st.subheader("🛠 Detected Skills")

    if skills:
        st.write(skills)
    else:
        st.warning("No skills detected.")

    # ATS Score
    ats_score = min(len(skills) * 10, 100)

    st.subheader("📊 ATS Score")

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=ats_score,
            title={"text": "ATS Score"},
            gauge={
                "axis": {"range": [0, 100]}
            }
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success(f"ATS Score: {ats_score}/100")

    # Resume Feedback
    st.subheader("🧠 Resume Feedback")

    feedback = []

    if len(skills) < 5:
        feedback.append(
            "Add more technical skills to strengthen your profile."
        )

    if "python" not in [s.lower() for s in skills]:
        feedback.append(
            "Python is highly recommended for Data Science roles."
        )

    if "sql" not in [s.lower() for s in skills]:
        feedback.append(
            "SQL is important for Analytics and Data Science jobs."
        )

    if ats_score < 70:
        feedback.append(
            "Add more projects and certifications to improve ATS score."
        )

    if feedback:
        for item in feedback:
            st.warning(item)
    else:
        st.success("Excellent Resume! Strong profile detected.")

    # JD Matching
    st.subheader("📋 Job Description Matching")

    job_description = st.text_area(
        "Paste Job Description Here"
    )

    if job_description:

        jd_skills = extract_skills(job_description)

        matching_skills = list(
            set(skills).intersection(jd_skills)
        )

        if len(jd_skills) > 0:
            match_percentage = int(
                (len(matching_skills) / len(jd_skills)) * 100
            )
        else:
            match_percentage = 0

        st.write(
            f"🎯 Resume Match Score: {match_percentage}%"
        )

        missing_skills = list(
            set(jd_skills) - set(skills)
        )

        if missing_skills:
            st.warning(
                "Missing Skills: " +
                ", ".join(missing_skills)
            )
        else:
            st.success(
                "Great! Your resume contains all detected JD skills."
            )

    # Recommended Roles
    jobs = match_jobs(skills)

    st.subheader("💼 Recommended Roles")

    for job in jobs:
        st.write(
            f"✅ {job['job']} — Match Score: {job['score']}"
        )

    # Skill Gap Analysis
    st.subheader("🎯 Skill Gap Analysis")

    required_skills = [
        "python",
        "sql",
        "power bi",
        "tableau",
        "machine learning",
        "pandas"
    ]

    missing = [
        skill for skill in required_skills
        if skill not in [s.lower() for s in skills]
    ]

    if missing:
        st.warning(
            "Skills to Learn: " + ", ".join(missing)
        )
    else:
        st.success(
            "You already have all core skills!"
        )

    # Career Roadmap
    st.subheader("🗺 Career Roadmap")

    top_job = jobs[0]["job"]

    if top_job == "Data Analyst":

        st.write("""
1. Master SQL
2. Learn Advanced Excel
3. Build Power BI Dashboards
4. Work on Data Analysis Projects
5. Apply for Data Analyst Roles
        """)

    elif top_job == "Data Scientist":

        st.write("""
1. Master Python
2. Learn Pandas and NumPy
3. Learn Machine Learning
4. Build End-to-End Projects
5. Apply for Data Scientist Roles
        """)

    elif top_job == "ML Engineer":

        st.write("""
1. Learn Deep Learning
2. Master TensorFlow
3. Build AI Projects
4. Learn Model Deployment
5. Apply for ML Engineer Roles
        """)

    elif top_job == "Business Analyst":

        st.write("""
1. Learn SQL
2. Master Excel
3. Learn Power BI
4. Build Business Dashboards
5. Apply for Business Analyst Roles
        """)

    # Profile Strength
    st.subheader("🏆 Profile Strength")

    if ats_score >= 80:
        st.success("Strong Profile")
    elif ats_score >= 60:
        st.info("Moderate Profile")
    else:
        st.error("Needs Improvement")
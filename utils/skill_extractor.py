SKILLS_DB = [
    "python",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "machine learning",
    "deep learning",
    "nlp",
    "tensorflow",
    "pandas",
    "numpy",
    "streamlit",
    "java"
]

def extract_skills(text):
    text = text.lower()
    skills = []

    for skill in SKILLS_DB:
        if skill in text:
            skills.append(skill)

    return skills
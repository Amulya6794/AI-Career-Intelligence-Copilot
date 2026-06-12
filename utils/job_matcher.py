SKILL_WEIGHTS = {
    "python": 3,
    "sql": 3,
    "excel": 2,
    "power bi": 2,
    "tableau": 2,
    "machine learning": 4,
    "deep learning": 4,
    "nlp": 3,
    "pandas": 3,
    "numpy": 3,
    "streamlit": 2,
    "tensorflow": 4
}

JOBS = {
    "Data Scientist": ["python", "machine learning", "pandas", "numpy", "nlp"],
    "Data Analyst": ["python", "sql", "excel", "power bi", "tableau"],
    "ML Engineer": ["python", "machine learning", "deep learning", "tensorflow"],
    "Business Analyst": ["excel", "sql", "power bi"]
}

def match_jobs(user_skills):
    results = []
    user_skills_clean = [skill.strip().lower() for skill in user_skills]
    
    for job_title, required_skills in JOBS.items():
        score = 0
        total_possible_score = 0
        matched_skills = []
        
        for skill in required_skills:
            skill_lower = skill.lower()
            weight = SKILL_WEIGHTS.get(skill_lower, 1)
            total_possible_score += weight
            
            if skill_lower in user_skills_clean:
                score += weight
                matched_skills.append(skill)
        
        # Calculate real percentage out of 100
        if total_possible_score > 0:
            percentage = int((score / total_possible_score) * 100)
        else:
            percentage = 0
        
        if percentage > 0:
            results.append({
                "job": job_title,
                "score": percentage,  # Actual 0-100% value
                "matched_skills": matched_skills
            })
            
    results.sort(key=lambda x: x["score"], reverse=True)
    return results
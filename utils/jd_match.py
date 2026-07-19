from utils.gemini import model
from utils.gemini import clean_json
import json

def match_resume(resume_text, job_description):
    prompt = f"""You are an ATS recruiter. Compare the resume with the job description.
            Return ONLY JSON.
            {{
            "match_score": 0,
            "matched_skills": [],
            "missing_skills": [],
            "feedback": "",
            "recommendation": ""}}

        Resume: {resume_text}
        Job Description: {job_description}"""
    
    response = model.generate_content(prompt)
    text = clean_json(response.text)
    try:
        return json.loads(text)
    except Exception:
        return {
            "match_score": 0,
            "matched_skills": [],
            "missing_skills": [],
            "feedback": "Could not compare.",
            "recommendation": ""
        }
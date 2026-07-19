import json
import os
import google.generativeai as genai
from dotenv import load_dotenv
from utils.prompts import PROMPT

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

def clean_json(text):
    #Remove markdown formatting from Gemini response.
    text = text.replace("```json", "")
    text = text.replace("```", "")
    return text.strip()

def analyze_resume(resume_text):
    response = model.generate_content(
        PROMPT + resume_text
    )
    cleaned = clean_json(response.text)
    try:
        result = json.loads(cleaned)
    except json.JSONDecodeError:
        return {
            "ats_score": 0,
            "summary": "Could not analyze resume.",
            "strengths": [],
            "weaknesses": [],
            "missing_skills": [],
            "improvement_tips": []
        }
    return result
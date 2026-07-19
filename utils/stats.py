import re

def resume_stats(text):
    #Calculate basic resume statistics.
    words = len(text.split())
    characters = len(text)
    lines = len(text.splitlines())
    email = bool(
        re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    )
    phone = bool(re.search(r"\+?\d[\d\s-]{8,}", text))
    github = "github" in text.lower()
    linkedin = "linkedin" in text.lower()
    return {
        "Words": words,
        "Characters": characters,
        "Lines": lines,
        "Email Found": "Yes" if email else "No",
        "Phone Found": "Yes" if phone else "No",
        "GitHub": "Yes" if github else "No",
        "LinkedIn": "Yes" if linkedin else "No",
    }
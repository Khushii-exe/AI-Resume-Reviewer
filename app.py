import streamlit as st
from utils.parser import extract_text
from utils.gemini import analyze_resume
from utils.stats import resume_stats
from utils.jd_match import match_resume
from utils.report import display_report, display_jd_report
from utils.styles import load_css

# Page Configuration
st.set_page_config(
    page_title="AI Resume Reviewer",
    page_icon="📄",
    layout="wide"
)

load_css()

st.title("📄 AI Resume Reviewer")
st.write(
    "Upload your resume and receive AI-powered feedback using Google's Gemini.")

st.divider()

with st.sidebar:
    st.header("About")
    st.write("""
This project reviews resumes using Google's Gemini API.

### Features
- ATS Score
- Resume Summary
- Strengths
- Weaknesses
- Missing Skills
- Improvement Tips
- Job Description Matching
""")

# Inputs
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)
job_description = st.text_area(
    "Paste Job Description (Optional)",
    height=200,
    placeholder="Paste the job description here..."
)

# Analyze Button
if st.button("Analyze Resume", use_container_width=True):
    if uploaded_file is None:
        st.warning("Please upload a resume.")
        st.stop()
    st.success(f"Uploaded: {uploaded_file.name}")
    # Extract resume text
    resume_text = extract_text(uploaded_file)
    if not resume_text.strip():
        st.error("Could not extract text from the uploaded resume.")
        st.stop()

    # Resume Statistics
    stats = resume_stats(resume_text)
    st.subheader("📄 Resume Statistics")
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Words", stats["Words"])
    col2.metric("Email", stats["Email Found"])
    col3.metric("Phone", stats["Phone Found"])
    col4.metric("GitHub", stats["GitHub"])

    col5, col6 = st.columns(2)

    col5.metric("LinkedIn", stats["LinkedIn"])
    col6.metric("Characters", stats["Characters"])

    st.divider()

    with st.expander("Preview Extracted Resume Text"):
        st.text_area(
            "",
            resume_text,
            height=250
        )

    with st.spinner("Reviewing your resume with Gemini AI..."):
        try:
            result = analyze_resume(resume_text)
            display_report(result)
            if job_description.strip():
                st.divider()
                jd_result = match_resume(
                    resume_text,
                    job_description
                )
                display_jd_report(jd_result)
        except Exception as e:

            st.error("Something went wrong while analyzing the resume.")
            st.code(str(e))
# 🤖 AI Resume Reviewer

An AI-powered Resume Reviewer built using **Streamlit** and **Google Gemini API** that analyzes resumes, provides ATS-friendly feedback, and matches resumes with job descriptions.

---

## 🚀 Features

- 📄 Upload resumes in **PDF** or **DOCX** format
- 🤖 AI-powered resume analysis using **Google Gemini**
- 📊 ATS Score prediction
- 💪 Highlights resume strengths
- ⚠️ Identifies weaknesses and missing skills
- 💡 Provides actionable improvement suggestions
- 📈 Resume statistics (word count, email, phone, GitHub, LinkedIn detection)
- 🎯 Job Description (JD) matching
- 📌 Skill gap analysis between resume and JD

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- pdfplumber
- python-docx
- python-dotenv

---

## 📂 Project Structure

```text
AI-Resume-Reviewer/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── utils/
│   ├── gemini.py
│   ├── parser.py
│   ├── prompts.py
│   ├── report.py
│   ├── stats.py
│   ├── jd_match.py
│   └── styles.py
│
└── assets/
```

### Resume Analysis

```
assets/analysis.png
```

---

### Job Description Matching

```
assets/jd-match.png
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Khushii-exe/AI-Resume-Reviewer.git
cd AI-Resume-Reviewer
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

You can obtain a free Gemini API key from:

https://aistudio.google.com/app/apikey

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📋 How It Works

1. Upload a resume (PDF/DOCX)
2. Resume text is extracted
3. Gemini AI analyzes the resume
4. ATS score and detailed feedback are generated
5. (Optional) Provide a Job Description
6. Resume is compared against the JD
7. Missing skills and improvement suggestions are displayed

---

## 📌 Future Improvements

- Downloadable PDF report
- Rule-based ATS scoring
- Resume keyword optimization
- Multiple resume comparison
- Dark mode
- Support for additional file formats

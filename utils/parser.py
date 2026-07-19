import pdfplumber
from docx import Document

def read_pdf(uploaded_file):
    """Extract text from PDF."""
    text = ""
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            print(f"Pages found: {len(pdf.pages)}")
            for page in pdf.pages:
                page_text = page.extract_text()
                print(page_text)
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(e)
    return text

def read_docx(uploaded_file):
    text = ""
    try:
        document = Document(uploaded_file)
        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"
    except Exception as e:
        print(e)
    return text

def extract_text(uploaded_file):
    filename = uploaded_file.name.lower()
    if filename.endswith(".pdf"):
        return read_pdf(uploaded_file)
    elif filename.endswith(".docx"):
        return read_docx(uploaded_file)
    return ""
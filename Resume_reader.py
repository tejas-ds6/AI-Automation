import pdfplumber
import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "python", "java", "c++", "machine learning","MATLAB","VS Code",
    "deep learning", "sql", "nlp", "tensorflow",
    "pandas", "opencv" , "HTML", "artificial intelligence","autocad","leadership"
]

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_skills(text):
    doc = nlp(text.lower())
    found_skills = []

    for token in doc:
        if token.text in SKILLS_DB:
            found_skills.append(token.text)

    return list(set(found_skills))

def parse_resume(file):
    text = extract_text_from_pdf(file)
    skills = extract_skills(text)

    return {"skills": skills}

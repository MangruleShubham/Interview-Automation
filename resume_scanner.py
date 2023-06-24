import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
import pandas as pd

nlp = spacy.load("en_core_web_sm")

# Define list of skills to match
skills_list = ['Python', 'Java', 'JavaScript', 'C++', 'SQL', 'AWS', 'Azure', 'Scrum', 'Agile', 'Project Management']

# Create phrase matcher with skill patterns
matcher = PhraseMatcher(nlp.vocab)
patterns = [nlp(skill) for skill in skills_list]
matcher.add("SKILLS", None, *patterns)

# Define function to extract skills from resume
def extract_skills(resume_path):
    with open(resume_path, 'r') as resume_file:
        resume_text = resume_file.read()
    
    doc = nlp(resume_text)
    matches = matcher(doc)
    
    skills = []
    for match_id, start, end in matches:
        skill_span = Span(doc, start, end, label=match_id)
        skills.append(skill_span.text)
    
    return skills

# Example usage
def start(path):
    resume_path = path
    skills = extract_skills(resume_path)
    return skills

import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
import pandas as pd
import os
import re
import smtplib
from email.message import EmailMessage

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

# Define function to extract email from resume
def extract_email(resume_path):
    with open(resume_path, 'r') as resume_file:
        resume_text = resume_file.read()
    
    email_regex = r'[\w\.-]+@[\w\.-]+\.\w+'
    email_match = re.search(email_regex, resume_text)
    if email_match:
        return email_match.group(0)
    else:
        return None

# Get the directory of shortlisted resumes from the user
shortlisted_resumes_directory = input("Please enter the directory of shortlisted resumes: ")

# Iterate over each resume in the directory
for filename in os.listdir(shortlisted_resumes_directory):
    if filename.endswith(".pdf") or filename.endswith(".txt"):
        resume_path = os.path.join(shortlisted_resumes_directory, filename)
        
        # Extract skills from the resume
        skills = extract_skills(resume_path)
        
        # Extract email from the resume
        email_address = extract_email(resume_path)
        
        if email_address:
            # Send email invitation
            email_password = "Mangrule@2001"  # Replace with your email password
            
            # Compose the email message
            msg = EmailMessage()
            msg["Subject"] = "Interview Invitation"
            msg["From"] = "vickeymangrule@gmail.com"
            msg["To"] = email_address
            
            # Add the Google Meet link to the email body
            google_meet_link = "https://meet.google.com/qce-bhog-gzk"  # Replace with your Google Meet link
            email_body = f"Dear Candidate,\n\nWe are pleased to invite you for an interview. Please join the interview using the following Google Meet link:\n\n{google_meet_link}\n\nThank you.\n\nBest regards,\nYour Company"
            msg.set_content(email_body)
            
            # Send the email
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(email_address, email_password)
                smtp.send_message(msg)
            
            print(f"Invitation email sent to {email_address} for resume: {filename}")
        else:
            print(f"No email address found in resume: {filename}")

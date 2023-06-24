import os
import re
from twilio.rest import Client

# Define function to extract email and phone number from resume
def extract_contact_info(resume_path):
    with open(resume_path, 'r') as resume_file:
        resume_text = resume_file.read()
    
    email_regex = r'[\w\.-]+@[\w\.-]+\.\w+'
    email_match = re.search(email_regex, resume_text)
    
    phone_regex = r'\+\d{12}'
 # Assuming the phone number format is 10 digits
    phone_match = re.search(phone_regex, resume_text)
    
    email_address = email_match.group(0) if email_match else None
    phone_number = phone_match.group(0) if phone_match else None
    
    return email_address, phone_number

# Get the directory of shortlisted resumes from the user
def send_message():
        
    shortlisted_resumes_directory = input("Please enter the directory of shortlisted resumes: ")

    # Initialize Twilio client
    account_sid = "AC6b833109c2b7d8bc9b66aecaf34e1980"
    auth_token = "4bd49a86ddd99e247b76b7139ffd5788"
    twilio_phone_number = "+12525168432"

    client = Client(account_sid, auth_token)

    # Iterate over each resume in the directory
    for filename in os.listdir(shortlisted_resumes_directory):
        if filename.endswith(".pdf") or filename.endswith(".txt"):
            resume_path = os.path.join(shortlisted_resumes_directory, filename)
            
            # Extract email and phone number from the resume
            email_address, phone_number = extract_contact_info(resume_path)
            
            if phone_number:
                # Send SMS via Twilio
                sms_body = f"Dear Candidate,\n\nCongratulations! You have been selected. Your key is {filename}.\n\nBest regards,\nYour Company"
                
                message = client.messages.create(
                    body=sms_body,
                    from_=twilio_phone_number,
                    to=phone_number
                )
                
                print(f"Selection SMS sent to {phone_number} for resume: {filename}")
            else:
                print(f"No phone number found in resume: {filename}")


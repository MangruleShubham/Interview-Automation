README Document for Interview Automation Project

Project Name: Interview Automation for HR

Description:
The Interview Automation for HR project is a backend process designed to automate the interview process for HR personnel. It aims to simplify resume shortlisting, candidate communication, and interview evaluation.

The project offers the following functionalities:

1. Resume Shortlisting:
   - HR personnel input specific skills they are looking for in a candidate's resume.
   - Resumes are processed, and skills mentioned in each resume are analyzed.
   - Resumes matching the desired skills are shortlisted for further evaluation.

2. Candidate Communication:
   - SMS and email notifications can be sent to the shortlisted candidates.
   - Contact details (email addresses, phone numbers) are extracted from the resumes to facilitate communication.

3. Interview Process:
   - Candidates receive a unique secret key via SMS, which serves as a reference during the interview.
   - During the interview, candidates' resumes are retrieved using the secret key.
   - A question and answer bank is maintained, relevant to the skills mentioned in the resume.
   - Candidates are asked questions related to their skills, and their answers are evaluated for correctness.
   - The evaluation is done using sentence mining similarity techniques.

Installation and Setup:
1. Clone the repository from GitHub: [GitHub Repository URL]
2. Install the required dependencies and libraries listed in the project's requirements.txt file.
3. Set up a database to store candidate resumes, question-answer pairs, and other relevant data.
4. Configure the database connection in the project's configuration file.
5. Run the project's main application file to start the backend process.

Usage:
1. HR personnel interact with the project via backend processes.
2. Provide the desired skills for resume shortlisting.
3. Upload candidate resumes for processing.
4. Utilize the system to send SMS and email notifications to shortlisted candidates.
5. During the interview, provide candidates with a unique secret key.
6. Ask interview questions related to the candidate's skills mentioned in the resume.
7. Evaluate the correctness of answers using sentence mining similarity techniques.

Contributing:
Contributions to enhance the functionality and performance of the Interview Automation for HR project are welcome. If you wish to contribute, please follow the guidelines mentioned in the CONTRIBUTING.md file.

License:
The Interview Automation for HR project is released under the [Shubham] license. Please review the license file for more details.

Contact:
For any inquiries or support regarding the project, please contact Shubham Mangrule at [shubham.mangrule20@vit.edu].

We appreciate your interest in the Interview Automation for HR project and look forward to your contributions!

import os
import re
import shutil

# Ask user for the folder directory
def shortlist():   
        
    folder_directory = input("Please enter the folder directory where the resumes are located: ")
    # Check if the provided directory exists
    if not os.path.isdir(folder_directory):
        print("Invalid directory. Please provide a valid folder directory.")
        exit()

    # Ask user for the skills
    skills = input("Please enter the skills (separated by commas): ")
    skills_list = [skill.strip().lower() for skill in skills.split(',')]

    # Create a new folder for shortlisted resumes
    shortlisted_folder = os.path.join(os.path.dirname(folder_directory), "shortlisted_resumes")
    os.makedirs(shortlisted_folder, exist_ok=True)

    # Open each resume and check for skills
    for filename in os.listdir(folder_directory):
        if filename.endswith(".txt") or filename.endswith(".docx"):
            resume_path = os.path.join(folder_directory, filename)

            with open(resume_path, 'r') as resume_file:
                resume_content = resume_file.read().lower()  # Convert content to lowercase

                # Count the number of skills present in the resume
                skills_found = 0
                for skill in skills_list:
                    # Use word-based matching with regular expressions
                    pattern = r'\b{}\b'.format(re.escape(skill))
                    if re.search(pattern, resume_content):
                        skills_found += 1

                # Check if the resume meets the criteria for shortlisting
                if skills_found >= len(skills_list) / 2:
                    # Create a new file for the shortlisted resume
                    shortlisted_filename = os.path.splitext(filename)[0] + "_shortlisted" + os.path.splitext(filename)[1]
                    shortlisted_path = os.path.join(shortlisted_folder, shortlisted_filename)

                    # Copy the resume to the shortlisted folder
                    shutil.copyfile(resume_path, shortlisted_path)

    print("Shortlisting process complete. The shortlisted resumes have been saved in the 'shortlisted_resumes' folder.")

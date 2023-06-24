import random
import os
from  answer_similarity import similarity_score
from resume_scanner import start

def record_answer():
    print("Write your answer:")
    return input()

def get_questions(skills_list):
    for skill in skills_list:
        try:
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{skill.lower()}_questions.txt")
            with open(file_path, "r") as f:
                lines = f.readlines()
                questions = []
                for i in range(0, len(lines), 2):
                    question = lines[i].strip()
                    answer = lines[i+1].strip() if i+1 < len(lines) else "No answer provided."
                    questions.append((question, answer))
                random_questions = random.sample(questions, k=min(len(questions), 3))
                print(f"\n{skill} Questions:")
                user_answers = []
                for q in random_questions:
                    print(f"Question: {q[0]}\n")
                    user_answer = record_answer()
                    user_answers.append((q[0], user_answer))
                    score=similarity_score(q[1],user_answer)
                    print(f"\nUser Answer: {user_answer}\n")
                    print(f"Answer: {q[1]}\n")
                    print(f"User answer similarity score: {score}\n")
                with open(f"{skill.lower()}_user_answers.txt", "w") as f:
                    for answer in user_answers:
                        f.write(f"{answer[0]}\nUser Answer: {answer[1]}\n Answer Similarity Score: {score}\n\n")
        except FileNotFoundError:
            print(f"No questions found for {skill}\n")

def start_interview():
        
    # Get the key from the user
    key = input("Please enter the key to search for: ")

    # Directory path of shortlisted resumes
    shortlisted_resumes_directory = "EDI\shortlisted_resumes"

    # Iterate over each file in the directory
    for filename in os.listdir(shortlisted_resumes_directory):
        if key in filename:
            file_path = os.path.join(shortlisted_resumes_directory, filename)
            skills_list=start(file_path)
    # Example usage: get questions for skills list
    
    get_questions(skills_list)
   

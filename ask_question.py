import random
import speech_recognition as sr
import sounddevice as sd
import scipy.io.wavfile as wavfile
import os
import io

def record_audio(duration, sample_rate=16000):
    print("Recording audio...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    print("Finished recording.")
    audio_io = io.BytesIO()
    wavfile.write(audio_io, sample_rate, audio_data)
    audio_io.seek(0)
    audio = sr.AudioData(audio_io.read(), sample_rate=sample_rate, sample_width=2)
    return audio

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
                    print(f"Question: {q[0]}")
                    print("Speak now!")
                    audio = record_audio(5)
                    recognizer = sr.Recognizer()
                    user_answer = ""
                    try:
                        user_answer = recognizer.recognize_google(audio)
                        user_answers.append((q[0], user_answer))
                        print(f"User Answer: {user_answer}")
                    except sr.UnknownValueError:
                        print("Sorry, I didn't understand.")
                    except sr.RequestError as e:
                        print(f"Sorry, an error occurred: {e}")
                    print(f"Answer: {q[1]}")
                with open(f"{skill.lower()}_user_answers.txt", "w") as f:
                    for answer in user_answers:
                        f.write(f"{answer[0]}\nUser Answer: {answer[1]}\n\n")
        except FileNotFoundError:
            print(f"No questions found for {skill}")

# Example usage: get questions for skills list
skills_list = ["Python", "Java", "Machine Learning"]
get_questions(skills_list)
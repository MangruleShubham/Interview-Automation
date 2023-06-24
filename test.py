# Function to check if a student passed in all subjects
def passed_all_subjects(marks):
    return all(mark >= 50 for mark in marks)

# Read the number of students
N = int(input())

# Dictionary to store students' details grouped by department
students = {}

# Iterate over each student
for _ in range(N):
    details = input().split()
    name = details[0]
    roll_no = details[1]
    marks = list(map(int, details[2:]))
    department = roll_no[:2]

    # Check if the student passed in all subjects
    if passed_all_subjects(marks):
        # Add the student to the corresponding department in the dictionary
        if department not in students:
            students[department] = []
        students[department].append((name, roll_no))

# Print the details of students who passed in all subjects
for department in sorted(students.keys()):
    for student in students[department]:
        print(f"{student[0]} {student[1]}")

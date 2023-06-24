from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Global variable to store the submitted code
submitted_code = ""

# Problem statement
problem_statement = """
Write a program that takes two numbers as input and prints their sum.

Input:
The input consists of two integers a and b separated by a space.

Output:
Print the sum of the two numbers.

Example:
Input: 3 4
Output: 7
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    global submitted_code
    
    if request.method == 'POST':
        # Read the code from the form
        code = request.form.get('code')
        language = request.form.get('language')

        # Save the submitted code
        submitted_code = code

        # Compile and run the code
        output = compile_and_run(code, language)

        # Render the template with the output and submitted code
        return render_template('index.html', problem_statement=problem_statement, output=output, code=submitted_code)
    else:
        # Render the template with the problem statement and submitted code
        return render_template('index.html', problem_statement=problem_statement, code=submitted_code)

def compile_and_run(code, language):
    # JDoodle API request
    url = "https://api.jdoodle.com/v1/execute"

    # Set the request payload
    payload = {
        "clientId": "MY",
        "clientSecret": "My",
        "script": code,
        "language": language,
        "versionIndex": "0"
    }

    # Send the request to the JDoodle API
    response = requests.post(url, json=payload)

    # Parse the response JSON
    response_data = response.json()

    if 'output' in response_data:
        # Get the output if available
        output = response_data['output']
        return output
    elif 'error' in response_data:
        # Get the error message if available
        error = response_data['error']
        return f"Compilation Error:\n{error}"
    else:
        return "Unknown error occurred."

if __name__ == '__main__':
    app.run(debug=True)

    #  'clientId': 'f373afb6baee446b161731e957f8037d',
    #     'clientSecret': 'd846d444fee75b07dc4bba5cee19e96906c999e3a9493525faaf104b6c55e4e9',

import requests

def compile_and_run(code, language):
    # JDoodle API request
    url = "https://api.jdoodle.com/v1/execute"

    # Set the request payload
    payload = {
        'clientId': 'f373afb6baee446b161731e957f8037d',
        'clientSecret': 'd846d444fee75b07dc4bba5cee19e96906c999e3a9493525faaf104b6c55e4e9',

        "script": code,
        "language": language,
        "versionIndex": "0"
    }

    # Send the request to the JDoodle API
    response = requests.post(url, json=payload)

    # Parse the response JSON
    response_data = response.json()

    # Get the output and error messages
    output = response_data["output"]
    error = response_data["error"]

    if error:
        return f"Compilation Error:\n{error}"
    else:
        return output

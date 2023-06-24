from sklearn.linear_model import LogisticRegression
import numpy as np

# Define the questions for each Ocean trait
questions = {
    "Openness": "Are you open to new experiences? (1 - Not at all, 5 - Very open): ",
    "Conscientiousness": "Are you generally organized and reliable? (1 - Not at all, 5 - Very much): ",
    "Extraversion": "Do you enjoy being around people and socializing? (1 - Not at all, 5 - Very much): ",
    "Agreeableness": "Are you generally considerate and cooperative? (1 - Not at all, 5 - Very much): ",
    "Neuroticism": "Do you often experience negative emotions? (1 - Not at all, 5 - Very much): "
}
def ask_questions():
    
        
    # Initialize an empty dictionary to store the user's responses
    user_responses = {}

    # Ask the user the questions and collect responses
    for trait, question in questions.items():
        response = input(question)
        user_responses[trait] = int(response)

    # Convert user responses to a feature vector
    feature_vector = np.array(list(user_responses.values())).reshape(1, -1)

    # Define the trained model
    model = LogisticRegression()

    model.coef_ = np.array([[0.012, 0.105, -0.024, 0.042, -0.083]])
    model.intercept_ = np.array([0.123])  # Add the intercept term

    # Fit the model to training data with binary labels (0 - Not Hired, 1 - Hired)
    X_train = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 1]])  # Example training data with 2 classes
    y_train = np.array([0, 1])  # Example training labels for the two classes
    model.fit(X_train, y_train)

    # Make predictions using the user's responses
    predicted_class = model.predict(feature_vector)

    # Print the predicted hiring decision
    if predicted_class[0] == 1:
        print("Hire the person.")

    else:
        print("Do not hire the person.")

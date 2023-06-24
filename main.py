from shortlisting_resume import shortlist
from send_sms import send_message
from presonality_prediction import ask_questions
from ask_questions import start_interview

# Define the menu function
def menu():
    print("Menu:")
    print("1. Shortlist")
    print("2. Send Message")
    print("3. Ask Questions")
    print("4. Start Interview")
    print("0. Exit")

    # Prompt the user for their choice
    choice = input("Enter your choice (0-4): ")

    # Call the function based on user's choice
    if choice == "1":
        shortlist()
    elif choice == "2":
        send_message()
    elif choice == "3":
        ask_questions()
    elif choice == "4":
        start_interview()
    elif choice == "0":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please try again.")

    # Recursive call to keep displaying the menu until the user chooses to exit
    menu()

# Call the menu function to start the program
menu()

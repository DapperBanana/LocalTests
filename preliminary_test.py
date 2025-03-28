
def personality_quiz():
    # Define the questions and possible answers
    questions = [
        "What is your favorite color?\nA) Blue\nB) Red\nC) Green",
        "What is your favorite animal?\nA) Dog\nB) Cat\nC) Bird",
        "What is your favorite season?\nA) Summer\nB) Winter\nC) Spring"
    ]
    
    # Define the possible personality types and the corresponding answers
    personality_types = {
        "Type A": ["A", "B", "C"],
        "Type B": ["B", "C", "A"],
        "Type C": ["C", "A", "B"]
    }
    
    # Initialize empty list to store user's answers
    user_answers = []
    
    # Ask user each question and store their answer
    for question in questions:
        print(question)
        answer = input("Enter your choice (A, B, or C): ").upper()
        user_answers.append(answer)
    
    # Calculate user's personality type based on their answers
    personality = ""
    for p_type, p_answers in personality_types.items():
        if user_answers == p_answers:
            personality = p_type
    
    # Print out the user's personality type
    if personality:
        print(f"Your personality type is: {personality}")
    else:
        print("Could not determine your personality type. Please try again.")
    
# Run the personality quiz
personality_quiz()

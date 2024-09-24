
def main():
    print("Welcome to the Personality Quiz!")
    
    # Questions and answers for the quiz
    questions = [
        "1. What is your favorite color?\nA) Red\nB) Blue\nC) Yellow\nD) Green",
        "2. What is your ideal way to spend a weekend?\nA) Relaxing at home\nB) Adventuring outdoors\nC) Going to a party\nD) Trying new things",
        "3. How do you handle stress?\nA) By meditating or practicing yoga\nB) By going for a run or exercising\nC) By talking to friends or family\nD) By working on a creative project"
    ]
    answers = ["A", "B", "C", "D"]
    
    # Dictionary to store the personality traits based on the answers
    personality_traits = {
        "A": "You are calm and collected.",
        "B": "You are adventurous and outgoing.",
        "C": "You are social and outgoing.",
        "D": "You are creative and innovative."
    }
    
    # Initialize empty list to store user's answers
    user_answers = []
    
    # Loop through the questions and get user's answers
    for question in questions:
        print(question)
        user_answer = input("Enter your choice (A/B/C/D): ").upper()
        while user_answer not in answers:
            print("Invalid choice. Please enter A, B, C, or D.")
            user_answer = input("Enter your choice (A/B/C/D): ").upper()
        user_answers.append(user_answer)
    
    # Calculate personality based on user's answers
    personality = []
    for answer in user_answers:
        personality.append(personality_traits[answer])
    
    # Display user's personality traits
    print("\nYour personality traits:")
    for trait in personality:
        print("- " + trait)
    
    print("\nThanks for taking the quiz!")
    
if __name__ == "__main__":
    main()

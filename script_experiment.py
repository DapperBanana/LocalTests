
def main():
    print("Welcome to the Personality Quiz!")
    
    questions = [
        "What is your favorite color?\nA) Red\nB) Blue\nC) Green\nD) Yellow",
        "What is your favorite season?\nA) Spring\nB) Summer\nC) Fall\nD) Winter",
        "What is your dream vacation destination?\nA) Beach\nB) Mountains\nC) City\nD) Countryside"
    ]
    
    answers = ['A', 'B', 'C', 'D']
    
    personality_results = {
        'A': 'You are outgoing and friendly.',
        'B': 'You are calm and introspective.',
        'C': 'You are ambitious and goal-oriented.',
        'D': 'You are down-to-earth and practical.'
    }
    
    user_answers = []
    
    for i, question in enumerate(questions):
        print(question)
        user_answer = input("Enter your choice (A/B/C/D): ").upper()
        
        while user_answer not in answers:
            print("Invalid choice. Please choose from A, B, C, or D.")
            user_answer = input("Enter your choice (A/B/C/D): ").upper()
        
        user_answers.append(user_answer)
    
    print("\nPersonality Analysis:")
    for answer in user_answers:
        print(personality_results[answer])
    
if __name__ == "__main__":
    main()

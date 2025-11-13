
def main():
    print("Welcome to the Personality Quiz!")
    
    questions = [
        "1. What is your favorite color?\nA. Red\nB. Blue\nC. Green\n",
        "2. What is your favorite animal?\nA. Dog\nB. Cat\nC. Bird\n",
        "3. How do you like to spend your free time?\nA. Reading\nB. Exercising\nC. Watching TV\n"
    ]
    
    answers = []
    
    for question in questions:
        answer = input(question).upper()
        while answer not in ['A', 'B', 'C']:
            print("Please select a valid option (A, B, or C).")
            answer = input(question).upper()
        
        answers.append(answer)
    
    personality_type = get_personality_type(answers)
    
    print(f"Your personality type is: {personality_type}")
    
def get_personality_type(answers):
    personality_types = {
        'ABC': 'Type A - Assertive and ambitious',
        'ACB': 'Type B - Creative and free-spirited',
        'BAC': 'Type C - Analytical and logical'
    }
    
    key = ''.join(answers)
    return personality_types.get(key, 'Type D - Undefined personality type')

if __name__ == "__main__":
    main()

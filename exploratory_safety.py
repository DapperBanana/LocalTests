
def main():
    print("Welcome to the Personality Quiz!")
    
    questions = [
        "1. What is your favorite color? (a) Red (b) Blue (c) Green",
        "2. What is your favorite animal? (a) Dog (b) Cat (c) Bird",
        "3. How do you like to spend your free time? (a) Reading (b) Watching movies (c) Going for a run",
    ]
    
    answers = []
    
    for question in questions:
        print(question)
        answer = input("Enter your choice (a, b, or c): ")
        while answer not in ['a', 'b', 'c']:
            print("Invalid choice. Please enter 'a', 'b', or 'c'.")
            answer = input("Enter your choice (a, b, or c): ")
        answers.append(answer)
    
    personality_type = ""
    
    for ans in answers:
        if ans == 'a':
            personality_type += 'A'
        elif ans == 'b':
            personality_type += 'B'
        else:
            personality_type += 'C'
    
    print("\nYour personality type is:", personality_type)
    
    if personality_type == 'AAA':
        print("You are a confident and ambitious person.")
    elif personality_type == 'BBB':
        print("You are a creative and introspective person.")
    elif personality_type == 'CCC':
        print("You are an outgoing and energetic person.")
    else:
        print("Your personality is a mix of different traits.")
    
if __name__ == "__main__":
    main()

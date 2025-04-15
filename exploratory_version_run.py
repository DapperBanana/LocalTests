
def main():
    print("Welcome to the Personality Quiz!")
    
    questions = [
        "What is your favorite color? (a) Red (b) Blue (c) Green",
        "What is your favorite animal? (a) Dog (b) Cat (c) Bird",
        "What is your favorite season? (a) Spring (b) Summer (c) Fall"
    ]
    
    answers = []
    
    for question in questions:
        print(question)
        answer = input("Enter your choice (a, b, or c): ")
        answers.append(answer)
    
    personality_type = calculate_personality_type(answers)
    
    print("\nYour personality type is: " + personality_type)


def calculate_personality_type(answers):
    score = 0
    
    for answer in answers:
        if answer == 'a':
            score += 1
        elif answer == 'b':
            score += 2
        elif answer == 'c':
            score += 3
    
    if score <= 5:
        return "Introvert"
    elif score <= 8:
        return "Ambivert"
    else:
        return "Extrovert"


if __name__ == "__main__":
    main()

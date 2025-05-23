
def main():
    personality_quiz()

def personality_quiz():
    print("Welcome to the Personality Quiz!")
    print("Answer each question with either 'A', 'B', 'C', or 'D'.")
    print("Let's get started!")

    questions = [
        "What is your favorite color?\nA. Red\nB. Blue\nC. Yellow\nD. Green",
        "What is your ideal weekend activity?\nA. Hiking\nB. Reading\nC. Shopping\nD. Watching movies",
        "How do you handle stress?\nA. Exercise\nB. Meditation\nC. Shopping\nD. Talking to friends",
        "What is your favorite type of music?\nA. Rock\nB. Classical\nC. Pop\nD. Jazz"
    ]

    answers = []

    for question in questions:
        print(question)
        answer = input("Your answer: ")
        while answer not in ['A', 'B', 'C', 'D']:
            print("Invalid answer! Please try again.")
            answer = input("Your answer: ")
        answers.append(answer)

    personality_type = determine_personality(answers)
    print("Your personality type is:", personality_type)

def determine_personality(answers):
    personality_types = {
        'AAAA': 'Type 1',
        'ABCD': 'Type 2',
        'ACDC': 'Type 3',
        'ADBD': 'Type 4'
    }

    answer_key = ''.join(answers)
    personality_type = personality_types.get(answer_key, "Type not determined")

    return personality_type

if __name__ == "__main__":
    main()

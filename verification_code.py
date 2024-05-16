
def main():
    print("Welcome to the Personality Quiz!")
    print("Answer the following questions to determine your personality type.")

    questions = [
        "1. What is your favorite color? \n A) Red \n B) Blue \n C) Green",
        "2. What is your favorite animal? \n A) Dog \n B) Cat \n C) Bird",
        "3. What is your ideal vacation spot? \n A) Beach \n B) Mountains \n C) City",
        "4. What type of music do you prefer? \n A) Pop \n B) Rock \n C) Classical",
        "5. What is your go-to leisure activity? \n A) Reading \n B) Exercising \n C) Watching TV",
    ]

    answers = []

    for i, question in enumerate(questions):
        print(question)
        answer = input("Enter your choice (A/B/C): ")
        answers.append(answer.upper())

    personality_type = calculate_personality_type(answers)
    print("Your personality type is: " + personality_type)


def calculate_personality_type(answers):
    score_A = answers.count('A')
    score_B = answers.count('B')
    score_C = answers.count('C')

    if score_A > score_B and score_A > score_C:
        return "Type A - Ambitious and outgoing"
    elif score_B > score_A and score_B > score_C:
        return "Type B - Creative and introspective"
    elif score_C > score_A and score_C > score_B:
        return "Type C - Easygoing and sociable"
    else:
        return "Mixed personality traits"

if __name__ == "__main__":
    main()

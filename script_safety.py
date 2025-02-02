
def run_quiz():
    questions = [
        "What is your favorite color?\nA) Red\nB) Blue\nC) Green\nD) Yellow\n",
        "What is your ideal vacation spot?\nA) Beach\nB) Mountains\nC) City\nD) Countryside\n",
        "What is your favorite type of music?\nA) Pop\nB) Rock\nC) Classical\nD) Hip hop\n"
    ]

    personality_types = {
        "A": "You are outgoing and adventurous.",
        "B": "You are calm and introspective.",
        "C": "You are intellectual and sophisticated.",
        "D": "You are energetic and creative."
    }

    answers = []
    for question in questions:
        answer = input(question).upper()
        if answer not in ['A', 'B', 'C', 'D']:
            print("Please select a valid option.")
            return
        answers.append(answer)

    personality_type = ""
    for answer in answers:
        personality_type += personality_types[answer] + " "

    print("Your personality type is:")
    print(personality_type)


run_quiz()

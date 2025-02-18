
def personality_quiz():
    questions = [
        "1. What is your favorite color?\nA. Blue\nB. Red\nC. Green\n",
        "2. What is your favorite animal?\nA. Dog\nB. Cat\nC. Bird\n",
        "3. What is your favorite season?\nA. Winter\nB. Summer\nC. Fall\n"
    ]
    
    answers = []
    
    for question in questions:
        answer = input(question).upper()
        answers.append(answer)
    
    score = 0
    for answer in answers:
        if answer == 'A':
            score += 1
        elif answer == 'B':
            score += 2
        elif answer == 'C':
            score += 3
    
    if score <= 4:
        print("Your personality is calm and peaceful.")
    elif score <= 7:
        print("Your personality is outgoing and adventurous.")
    elif score <= 9:
        print("Your personality is creative and imaginative.")
    else:
        print("Your personality is a mix of different traits.")
    
if __name__ == '__main__':
    personality_quiz()

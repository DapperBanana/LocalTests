
def print_question(question):
    print(question)
    answer = input("Enter your answer (A, B, C, D): ").upper()
    return answer

def calculate_score(answers):
    score = 0
    for ans in answers:
        if ans == "A":
            score += 1
        elif ans == "B":
            score += 2
        elif ans == "C":
            score += 3
        elif ans == "D":
            score += 4
    return score

def get_personality(score):
    if score <= 6:
        return "You are an introvert."
    elif score <= 12:
        return "You are an ambivert."
    elif score <= 18:
        return "You are an extrovert."
    else:
        return "You are a social butterfly!"

questions = [
    "1. When making big decisions, do you prefer to:\nA) Make a decision quickly\nB) Consider all options carefully\nC) Get advice from others\nD) Trust your gut instinct",
    "2. How do you feel about social events?\nA) Love them, always up for a party\nB) Enjoy them in moderation\nC) Prefer one-on-one interactions\nD) Avoid them at all costs",
    "3. How do you recharge after a long day?\nA) Spend time with friends\nB) Solitary activities like reading or watching TV\nC) Exercise or go for a walk\nD) Take a nap"
]

answers = []

for question in questions:
    answer = print_question(question)
    answers.append(answer)

score = calculate_score(answers)
personality = get_personality(score)

print("Your personality type is:", personality)

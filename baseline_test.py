
def main():
    print("Welcome to the Personality Quiz!")
    
    questions = [
        "1. What is your favorite color? \nA. Blue \nB. Red \nC. Yellow \nD. Green",
        "2. What is your ideal way to spend a day off? \nA. Relaxing at home \nB. Exploring a new city \nC. Trying a new hobby \nD. Spending time with friends and family",
        "3. How do you handle stress? \nA. Meditate or practice yoga \nB. Exercise or go for a run \nC. Talk to a friend or therapist \nD. Take a nap or watch TV",
    ]
    
    answers = []
    
    for question in questions:
        print(question)
        answer = input("Enter your answer (A, B, C, or D): ")
        answers.append(answer.upper())
    
    result = calculate_result(answers)
    
    print("\nYour personality type is: " + result)
    
def calculate_result(answers):
    a_count = answers.count('A')
    b_count = answers.count('B')
    c_count = answers.count('C')
    d_count = answers.count('D')
    
    max_count = max(a_count, b_count, c_count, d_count)
    
    if max_count == a_count:
        return "Introverted and thoughtful"
    elif max_count == b_count:
        return "Adventurous and outgoing"
    elif max_count == c_count:
        return "Creative and curious"
    else:
        return "Relaxed and easygoing"
    
if __name__ == "__main__":
    main()

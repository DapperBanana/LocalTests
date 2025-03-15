
def personality_quiz():
    print("Welcome to the Personality Quiz!")
    
    questions = ["1. What is your favorite color?", 
                 "2. What is your favorite season?", 
                 "3. Are you a morning person or a night owl?"]
    
    answers = []
    
    for question in questions:
        print(question)
        answer = input("Enter your answer: ")
        answers.append(answer)
    
    personality_type = determine_personality(answers)
    
    print("Your personality type is: ", personality_type)

def determine_personality(answers):
    color = answers[0].lower()
    season = answers[1].lower()
    time = answers[2].lower()
    
    if color == 'blue' and season == 'fall' and time == 'night owl':
        return "You are an introverted and artistic personality."
    elif color == 'red' and season == 'summer' and time == 'morning person':
        return "You are an extroverted and adventurous personality."
    elif color == 'green' and season == 'spring' and time == 'morning person':
        return "You are a calm and nurturing personality."
    else:
        return "Your personality type is hard to define. You are unique!"
        
personality_quiz()

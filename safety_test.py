
def main():
    print("Welcome to the Personality Quiz!")
    
    #Questions for the quiz
    questions = [
        "What is your favorite color?\nA. Red\nB. Blue\nC. Green\n",
        "What is your ideal way to spend a weekend?\nA. Relaxing at home\nB. Exploring the outdoors\nC. Hanging out with friends\n",
        "How do you handle stress?\nA. Meditate or do yoga\nB. Exercise\nC. Talk to someone about it\n"
    ]
    
    #Possible personality types based on user's responses
    personality_types = {
        "A": "You are calm and collected.",
        "B": "You are adventurous and outgoing.",
        "C": "You are social and outgoing."
    }
    
    #Initialize score for each personality type
    scores = {
        "A": 0,
        "B": 0,
        "C": 0
    }
    
    #Iterate through questions, get user input, and update scores
    for question in questions:
        answer = input(question)
        if answer.upper() in ["A", "B", "C"]:
            scores[answer.upper()] += 1
    
    #Determine the user's personality type based on scores
    personality_type = max(scores, key=scores.get)
    
    #Print the user's personality type
    print("\nYour personality type is: " + personality_types[personality_type])

if __name__ == "__main__":
    main()

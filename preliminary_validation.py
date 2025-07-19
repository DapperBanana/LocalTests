
def main():
    print("Welcome to the Personality Quiz!")
    
    # Questions to ask the user
    questions = [
        "1. What is your favorite color?\n A) Red\n B) Blue\n C) Green\n",
        "2. What is your ideal way to spend a day off?\n A) Relaxing at home\n B) Going on an adventure\n C) Hanging out with friends\n",
        "3. What is your preferred mode of transportation?\n A) Walking\n B) Car\n C) Bicycle\n",
        "4. How do you handle stress?\n A) Meditate\n B) Exercise\n C) Talk to a friend\n",
        "5. What do you value most in a friendship?\n A) Loyalty\n B) Fun\n C) Support\n"
    ]
    
    # Score to keep track of user responses
    score = {'A': 0, 'B': 0, 'C': 0}
    
    # Loop through each question and record user's response
    for question in questions:
        response = input(question).upper()
        
        if response in score:
            score[response] += 1
        else:
            print("Invalid response. Please choose A, B, or C.")
    
    # Determine the personality type based on the user's responses
    personality_type = max(score, key=score.get)
    
    # Display the result to the user
    print("Your personality type is: ", end='')
    if personality_type == 'A':
        print("Type A - Ambitious and competitive")
    elif personality_type == 'B':
        print("Type B - Cautious and reflective")
    elif personality_type == 'C':
        print("Type C - Sociable and caring")

if __name__ == "__main__":
    main()

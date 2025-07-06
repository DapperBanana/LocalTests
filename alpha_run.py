
def main():
    print("Welcome to the Personality Quiz!")
    print("Answer the following questions to determine your personality type.")
    
    # Questions and corresponding choices
    questions = [
        "What is your favorite color?\nA. Red\nB. Blue\nC. Green\n",
        "What is your ideal way to spend a weekend?\nA. Hiking in nature\nB. Relaxing at home\nC. Hanging out with friends\n",
        "How do you handle stress?\nA. Exercise\nB. Meditate\nC. Talk to someone\n"
    ]
    
    # Result options for each personality type
    results = {
        "A": "You are adventurous and outgoing!",
        "B": "You are calm and introspective!",
        "C": "You are sociable and empathetic!"
    }
    
    # Initialize personality type counters
    personality_types = {
        "A": 0,
        "B": 0,
        "C": 0
    }
    
    # Ask questions and record answers
    for i in range(len(questions)):
        answer = input(questions[i]).upper()
        
        if answer in results:
            personality_types[answer] += 1
        else:
            print("Invalid choice. Please choose A, B, or C.")
    
    # Determine the dominant personality type
    dominant_type = max(personality_types, key=personality_types.get)
    
    # Display result
    print("\nYour personality type is:", results[dominant_type])
    
if __name__ == "__main__":
    main()

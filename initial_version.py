
def main():
    print("Welcome to the Personality Quiz!")
    print("Answer the following questions to find out more about your personality.")

    # Questions
    questions = [
        "What is your favorite color? (a) Red (b) Blue (c) Green",
        "What is your ideal vacation spot? (a) Beach resort (b) Mountain cabin (c) City tour",
        "How do you handle stress? (a) Exercise (b) Meditate (c) Talk to a friend"
    ]

    # Personality traits
    traits = {"a": "Adventurous", "b": "Introverted", "c": "Social"}

    # Initialize personality trait counts
    trait_counts = {"Adventurous": 0, "Introverted": 0, "Social": 0}

    # Ask questions and keep track of answers
    for question in questions:
        answer = input(question + " ")
        if answer.lower() in ['a', 'b', 'c']:
            trait = traits[answer.lower()]
            trait_counts[trait] += 1

    # Determine personality type based on responses
    personality_type = max(trait_counts, key=trait_counts.get)

    print("\nYour personality type is: " + personality_type)

if __name__ == "__main__":
    main()

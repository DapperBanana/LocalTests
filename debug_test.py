
def main():
    print("Welcome to the personality quiz!")
    print("Answer each question with a number from 1 to 5, where 1 is strongly disagree and 5 is strongly agree.")

    # Questions for the quiz
    questions = [
        "I enjoy meeting new people.",
        "I prefer to stay at home rather than go out.",
        "I like to take risks and try new things.",
        "I am a good listener and enjoy helping others.",
        "I prefer to plan things out rather than be spontaneous."
    ]

    # Initialize score for each personality trait
    extroversion = 0
    introversion = 0
    openness = 0
    agreeableness = 0
    conscientiousness = 0

    # Ask the user each question
    for i, question in enumerate(questions, 1):
        answer = int(input(f"{question} (1-5): "))
        if i == 1 or i == 3:
            extroversion += answer
        elif i == 2 or i == 4:
            introversion += answer
        else:
            openness += answer
            agreeableness += answer
            conscientiousness += answer

    # Determine personality based on scores
    if extroversion > introversion:
        extroverted = True
    else:
        extroverted = False

    if openness > agreeableness and openness > conscientiousness:
        personality_trait = "open-minded"
    elif agreeableness > openness and agreeableness > conscientiousness:
        personality_trait = "kind-hearted"
    else:
        personality_trait = "responsible"

    # Display personality result
    print("\nYour personality profile:")
    print(f"Extroversion: {extroversion}")
    print(f"Introversion: {introversion}")
    print(f"Openness: {openness}")
    print(f"Agreeableness: {agreeableness}")
    print(f"Conscientiousness: {conscientiousness}")
    print(f"You are a {personality_trait} {'extrovert' if extroverted else 'introvert'}.")

if __name__ == "__main__":
    main()

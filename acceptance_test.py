
def personality_quiz():
    print("Welcome to the Personality Quiz!")
    print("Please answer the following questions with a number from 1 to 5 (1 being strongly disagree and 5 being strongly agree).")

    questions = [
        "I am a social butterfly and enjoy being around people.",
        "I prefer spending time alone rather than in a group setting.",
        "I am very organized and like to plan things ahead of time.",
        "I am spontaneous and enjoy going with the flow.",
        "I am a very analytical person who enjoys problem-solving.",
        "I am creative and enjoy expressing myself through art or music.",
        "I am a very competitive person and enjoy winning.",
        "I am a laid-back person who prefers a chill and relaxed atmosphere."
    ]

    personality_traits = {
        "Introverted": 0,
        "Extroverted": 0,
        "Organized": 0,
        "Spontaneous": 0,
        "Analytical": 0,
        "Creative": 0,
        "Competitive": 0,
        "Laid-back": 0
    }

    for i, question in enumerate(questions):
        response = int(input(f"{question} "))
        personality_traits["Extroverted" if i == 0 else "Introverted"] += response   # reverse for first question
        personality_traits["Organized" if i == 2 else "Spontaneous"] += response     # reverse for third question
        personality_traits["Analytical" if i == 4 else "Creative"] += response        # reverse for fifth question
        personality_traits["Competitive" if i == 6 else "Laid-back"] += response       # reverse for seventh question

    print("\nPersonality Traits:")
    for trait, score in personality_traits.items():
        print(f"{trait}: {score}")

    max_trait = max(personality_traits, key=personality_traits.get)
    print(f"\nYour dominant personality trait is: {max_trait}")

personality_quiz()

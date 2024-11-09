
def quiz():
    print("Welcome to the Personality Quiz! Please answer the following questions:")
    name = input("What is your name? ")

    score = 0

    print("Question 1: What is your favorite color?")
    color = input("a) Red\nb) Blue\nc) Yellow\n")

    if color.lower() == "a":
        score += 1
    elif color.lower() == "b":
        score += 2
    elif color.lower() == "c":
        score += 3

    print("Question 2: What is your favorite animal?")
    animal = input("a) Dog\nb) Cat\nc) Bird\n")

    if animal.lower() == "a":
        score += 1
    elif animal.lower() == "b":
        score += 2
    elif animal.lower() == "c":
        score += 3

    print("Question 3: What is your favorite food?")
    food = input("a) Pizza\nb) Salad\nc) Burger\n")

    if food.lower() == "a":
        score += 1
    elif food.lower() == "b":
        score += 2
    elif food.lower() == "c":
        score += 3

    if score <= 3:
        personality = "You are a calm and collected person."
    elif score <= 6:
        personality = "You are a friendly and outgoing person."
    else:
        personality = "You are an energetic and adventurous person."

    print(f"Thank you, {name}! Your personality is: {personality}")

quiz()

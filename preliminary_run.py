
print("Welcome to the Personality Quiz!")
print("Please answer the following questions with 'A', 'B', or 'C'.")

def get_input(question, options):
    while True:
        response = input(question + "\n" + options + "\n").upper()
        if response in ['A', 'B', 'C']:
            return response
        else:
            print("Invalid input. Please try again.")

score = 0

q1 = get_input("1. What is your favorite color?", "A. Red\nB. Blue\nC. Green")
if q1 == 'A':
    score += 1
elif q1 == 'B':
    score += 2
elif q1 == 'C':
    score += 3

q2 = get_input("2. What is your favorite animal?", "A. Dog\nB. Cat\nC. Bird")
if q2 == 'A':
    score += 1
elif q2 == 'B':
    score += 2
elif q2 == 'C':
    score += 3

q3 = get_input("3. What is your favorite food?", "A. Pizza\nB. Sushi\nC. Salad")
if q3 == 'A':
    score += 1
elif q3 == 'B':
    score += 2
elif q3 == 'C':
    score += 3

if score <= 4:
    result = "You have a calm and easy-going personality."
elif score <= 8:
    result = "You have a fun and adventurous personality."
else:
    result = "You have a creative and artistic personality."

print("Your personality result: " + result)

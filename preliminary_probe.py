
import random

def explore():
    print("You are on a space exploration mission.")
    print("You can choose to explore planets or asteroids.")
    choice = input("Enter 'planet' or 'asteroid' to explore: ")

    if choice.lower() == 'planet':
        explore_planet()
    elif choice.lower() == 'asteroid':
        explore_asteroid()
    else:
        print("Invalid choice. Please try again.")
        explore()

def explore_planet():
    planets = ["Mars", "Jupiter", "Saturn", "Neptune"]
    planet = random.choice(planets)
    
    print(f"You have landed on {planet}.")
    
    if planet == "Mars":
        print("You have discovered signs of past life on Mars!")
    elif planet == "Jupiter":
        print("You found a strange portal on Jupiter!")
    elif planet == "Saturn":
        print("You found a rare mineral on Saturn!")
    elif planet == "Neptune":
        print("You spotted a mysterious creature in the oceans of Neptune!")

def explore_asteroid():
    asteroid = random.randint(1, 100)
    
    print(f"You have landed on asteroid number {asteroid}.")
    
    if asteroid % 2 == 0:
        print("You found valuable minerals on the asteroid!")
    else:
        print("You encountered space pirates on the asteroid!")

explore()

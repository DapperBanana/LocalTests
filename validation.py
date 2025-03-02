
import random

def show_options():
    print("\nWhat would you like to do?")
    print("1. Explore a new planet")
    print("2. Gather resources")
    print("3. Refuel your spaceship")
    print("4. Quit the game")

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
resources = {"fuel": 100, "food": 100, "water": 100}

print("Welcome to the Space Exploration Game!")
print("You are the captain of a spaceship and your goal is to explore new planets.")

while True:
    show_options()
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        planet = random.choice(planets)
        print(f"You have landed on {planet}.")
        resources["fuel"] -= 20
        resources["food"] -= 10
        resources["water"] -= 10
    elif choice == "2":
        print("Gathering resources...")
        resources["fuel"] += 20
        resources["food"] += 10
        resources["water"] += 10
    elif choice == "3":
        print("Refueling your spaceship...")
        resources["fuel"] = 100
    elif choice == "4":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice, please try again.")

    print("Resources:")
    for item, amount in resources.items():
        print(f"{item}: {amount}")

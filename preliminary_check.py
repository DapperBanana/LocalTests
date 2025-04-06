
import random

def explore_planet():
    print("You have arrived at a new planet!")
    planets = ['Mars', 'Jupiter', 'Saturn', 'Neptune', 'Mercury']
    current_planet = random.choice(planets)
    print(f"You are now on planet {current_planet}")
    resources = random.randint(1, 10)
    print(f"You have found {resources} resources on this planet.")

def start_exploration():
    print("Welcome to the Space Exploration Game!")
    
    while True:
        choice = input("Do you want to explore a new planet? (yes/no): ")
        
        if choice.lower() == 'yes':
            explore_planet()
        elif choice.lower() == 'no':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

start_exploration()

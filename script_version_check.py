
import random

def explore_space():
    print("Welcome to the Space Exploration Game!")
    print("You are a space explorer on a mission to discover new planets.")
    
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    while True:
        choice = input("Do you want to explore a new planet? (yes/no): ").lower()
        
        if choice == "yes":
            planet = random.choice(planets)
            print(f"You have arrived at {planet}.")
            print("You can explore the planet, mine for resources, or move on to the next planet.")
            
            action = input("What would you like to do? (explore/mine/move on): ").lower()
            
            if action == "explore":
                print("You have explored the planet and found some interesting rock formations.")
            elif action == "mine":
                print("You have mined for resources and found some valuable minerals.")
            elif action == "move on":
                print("You have moved on to the next planet.")
            else:
                print("Invalid input. Please try again.")
        elif choice == "no":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid input. Please try again.")

explore_space()

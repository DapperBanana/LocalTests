
import random

def explore():
    print("Welcome to the Space Exploration Game!")
    player_name = input("Enter your name: ")
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    
    print(f"Welcome, {player_name}! You are now in your spaceship ready to explore the galaxy.")
    
    while True:
        command = input("Do you want to explore a new planet? (yes/no) ")
        if command.lower() == 'yes':
            planet = random.choice(planets)
            print(f"You have reached the planet {planet}.")
            resources = random.randint(1, 10)
            print(f"You have found {resources} resources on this planet.")
        elif command.lower() == 'no':
            print("Thanks for playing the Space Exploration Game!")
            break
        else:
            print("Invalid command. Please enter yes or no.")

explore()

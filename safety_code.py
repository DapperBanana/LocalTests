
import random

# Define a list of planets
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Define a list of possible events
events = ["Asteroid belt ahead! Maneuver through it carefully.", "Encounter alien life forms!", "Discover a new planet!", "Solar flare detected. Take cover!"]

print("Welcome to the Space Exploration Game!")
print("You are starting your journey from Earth.")

while True:
    user_input = input("Do you want to continue exploring? (yes/no): ")
    
    if user_input.lower() == "no":
        print("Thanks for playing! Goodbye.")
        break
    
    print("-----------------------------------------")
    
    # Randomly select a planet to explore
    current_planet = random.choice(planets)
    print("You are now on planet", current_planet)
    
    # Simulate a random event
    random_event = random.choice(events)
    print("Event:", random_event)
    
    print("-----------------------------------------")

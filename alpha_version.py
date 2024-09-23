
import random

# set initial values
fuel = 100
credits = 0
current_planet = "Earth"
planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
prices = {"Mercury": 10, "Venus": 20, "Mars": 30, "Jupiter": 40, "Saturn": 50, "Uranus": 60, "Neptune": 70}

# main game loop
while True:
    print(f"\nYou are currently on {current_planet}. Fuel: {fuel}, Credits: {credits}")

    # check if out of fuel
    if fuel <= 0:
        print("You ran out of fuel! Game over.")
        break

    # ask player for next action
    action = input("Do you want to refuel, travel to a new planet, or quit? ").lower()

    if action == "refuel":
        fuel += 50
        credits -= 10
        print("You refueled your spaceship and paid 10 credits.")
    
    elif action == "travel":
        new_planet = random.choice(planets)
        distance = abs(planets.index(new_planet) - planets.index(current_planet))

        fuel_needed = distance * 10
        if fuel >= fuel_needed:
            fuel -= fuel_needed
            credits += prices[new_planet]
            current_planet = new_planet
            print(f"You traveled to {new_planet} and earned {prices[new_planet]} credits.")
        else:
            print("You don't have enough fuel to travel to a new planet.")
    
    elif action == "quit":
        print("Thanks for playing! Goodbye.")
        break
    
    else:
        print("Invalid input. Please try again.")

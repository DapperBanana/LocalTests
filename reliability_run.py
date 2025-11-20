
import random

def display_intro():
    print("Welcome to the Space Adventure Game!")
    print("You are the captain of a spaceship on a mission to explore the galaxy.")
    print("Your objective is to safely reach the end of your journey.")
    print()

def choose_action():
    print("Choose your action:")
    print("1. Travel to a new planet")
    print("2. Refuel your spaceship")
    print("3. Check your current status")
    return input("Enter your choice (1-3): ")

def travel_to_planet():
    planets = ["Mars", "Jupiter", "Saturn", "Neptune"]
    planet = random.choice(planets)
    print("Traveling to", planet)
    return planet

def refuel():
    fuel = random.randint(50, 100)
    print("Refueling spaceship with", fuel, "units of fuel")
    return fuel

def check_status(fuel, distance):
    print("Current Status:")
    print("Fuel: ", fuel)
    print("Distance to destination: ", distance)
    print()

def main():
    display_intro()

    fuel = 100
    distance = 500

    while distance > 0:
        action = choose_action()

        if action == "1":
            planet = travel_to_planet()
            distance -= random.randint(50, 100)
            print("You have reached", planet)
        elif action == "2":
            fuel += refuel()
        elif action == "3":
            check_status(fuel, distance)
        else:
            print("Invalid choice, please try again.")

        if fuel <= 0:
            print("You are out of fuel, game over!")
            break

    if distance <= 0:
        print("Congratulations! You have safely reached your destination.")

if __name__ == "__main__":
    main()

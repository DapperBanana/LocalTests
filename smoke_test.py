
import random

def explore_planet(planet_name):
    print(f"You have arrived at planet {planet_name}!")
    print("Would you like to explore the planet?")

    choice = input("Enter 'yes' or 'no': ")

    if choice.lower() == "yes":
        print("You start exploring the planet...")
        resources = random.randint(1, 10)
        print(f"You found {resources} resources on this planet!")

        return resources
    else:
        print("You decide to leave the planet.")
        return 0

def main():
    resources = 0
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    print("Welcome to the space exploration game!")
    print("You have a spaceship and a limited amount of fuel.")
    print("Your goal is to explore as many planets as possible and collect resources.")

    while True:
        print(f"Current resources: {resources}")
        print("Choose a planet to explore:")
        for i, planet in enumerate(planets):
            print(f"{i+1}. {planet}")

        choice = int(input("Enter the planet number to explore (or 0 to exit): "))

        if choice == 0:
            print("Thank you for playing!")
            break
        elif choice < 1 or choice > len(planets):
            print("Invalid choice. Please try again.")
        else:
            resources += explore_planet(planets[choice - 1])

if __name__ == "__main__":
    main()

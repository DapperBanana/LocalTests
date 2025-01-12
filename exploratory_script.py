
import random

def explore_planet():
    planets = ['Mars', 'Jupiter', 'Saturn', 'Neptune', 'Uranus']
    planet = random.choice(planets)
    print(f"You have arrived at {planet}!")
    action = input("Do you want to explore the planet? (yes/no): ").lower()
    if action == 'yes':
        print("You have found some valuable resources on the planet!")
    else:
        print("You have decided to continue your journey through space.")

def main():
    print("Welcome to the Space Exploration Game!")
    while True:
        choice = input("Do you want to explore a new planet? (yes/no): ").lower()
        if choice == 'yes':
            explore_planet()
        else:
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()

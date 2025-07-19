
import random

def explore_planet(planet_name):
    resources = random.randint(1, 10)
    print(f"You have reached {planet_name}!")
    print(f"You have found {resources} resources.")
    return resources

def main():
    resources = 0
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    while True:
        choice = input("Do you want to explore a planet? (yes/no): ")
        
        if choice.lower() == "yes":
            planet = random.choice(planets)
            resources += explore_planet(planet)
        elif choice.lower() == "no":
            print("Game over. Total resources collected:", resources)
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()

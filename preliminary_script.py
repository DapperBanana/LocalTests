
import random

def explore_planet():
    planet_names = ["Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
    planet = random.choice(planet_names)
    resources = random.randint(1, 10)
    
    print(f"You have landed on the planet {planet}!")
    print(f"You have discovered {resources} resources.")
    
    return resources

def main():
    player_resources = 0
    while True:
        choice = input("Would you like to explore a planet? (yes/no): ")
        
        if choice.lower() == "yes":
            player_resources += explore_planet()
        elif choice.lower() == "no":
            print(f"You have collected a total of {player_resources} resources. Thanks for playing!")
            break
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()

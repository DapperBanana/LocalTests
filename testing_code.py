
import random

def explore_planet():
    planet_types = ['rocky', 'ice', 'gas']
    planet_type = random.choice(planet_types)
    print(f"You have landed on a {planet_type} planet.")
    
    if planet_type == 'rocky':
        print("You found some minerals on the planet.")
    elif planet_type == 'ice':
        print("You discovered a frozen lake on the planet.")
    else:
        print("You spotted a giant gas storm on the planet.")
    
def main():
    print("Welcome to the Space Exploration Game!")
    
    while True:
        command = input("What would you like to do? (explore/quit) ").lower()
        
        if command == 'explore':
            explore_planet()
        elif command == 'quit':
            print("Thanks for playing the Space Exploration Game!")
            break
        else:
            print("Invalid command. Please try again.")
            
if __name__ == "__main__":
    main()


import random

def explore_planet():
    resources = ['Gold', 'Silver', 'Diamonds', 'Alien technology']
    planet = random.choice(['Mars', 'Jupiter', 'Saturn', 'Neptune'])
    resource = random.choice(resources)
    print(f"You have landed on planet {planet}!")
    print(f"You have discovered {resource} on this planet.")
    
def space_battle():
    enemy_ships = ['Alien invaders', 'Space pirates', 'Rogue AI']
    enemy = random.choice(enemy_ships)
    print(f"You have encountered {enemy}!")
    print("Prepare for battle!")
    
def main():
    print("Welcome to the Space Exploration Game!")
    
    while True:
        choice = input("Would you like to explore a planet or engage in a space battle? (explore/battle/quit): ")
        
        if choice == 'explore':
            explore_planet()
        elif choice == 'battle':
            space_battle()
        elif choice == 'quit':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()

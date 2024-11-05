
import random

def explore_planet():
    planets = ['Mars', 'Venus', 'Jupiter', 'Saturn', 'Neptune']
    planet = random.choice(planets)
    print(f'Exploring planet {planet}...')
    
    minerals = ['gold', 'silver', 'diamonds', 'uranium', 'platinum']
    mineral = random.choice(minerals)
    print(f'Found a deposit of {mineral} on {planet}!')
    
    aliens = ['Martians', 'Venusians', 'Jovians', 'Saturnians', 'Neptunians']
    alien = random.choice(aliens)
    print(f'Encountered friendly {alien} on {planet}.')
    
def main():
    print('Welcome to the Space Exploration Game!')
    
    while True:
        choice = input('Would you like to explore a new planet? (yes/no): ')
        
        if choice.lower() == 'yes':
            explore_planet()
        else:
            print('Thanks for playing!')
            break

if __name__ == '__main__':
    main()

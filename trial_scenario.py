
import random

def display_intro():
    print("Welcome to Space Explorer!")
    print("You are the captain of a spaceship on a mission to explore the universe.")
    print("Your goal is to visit as many planets as possible and collect resources.")
    print("But watch out for asteroids and enemy ships along the way!")
    print("Good luck!\n")

def explore_planet():
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    current_planet = random.choice(planets)
    resources = random.randint(1, 10)

    print("You have arrived at " + current_planet)
    print("You have collected " + str(resources) + " resources.\n")

    return resources

def encounter_asteroid():
    print("Oh no! You have encountered an asteroid field.")
    damage = random.randint(1, 5)
    print("Your ship has taken " + str(damage) + " damage.\n")

    return damage

def encounter_enemy():
    print("Warning! Enemy ships are approaching.")
    num_enemy_ships = random.randint(1, 3)
    damage = num_enemy_ships * random.randint(1, 3)
    print("Your ship has taken " + str(damage) + " damage.\n")

    return damage

def main():
    display_intro()

    total_resources = 0
    total_damage = 0

    while True:
        action = input("Do you want to explore a planet? (y/n): ")
        
        if action.lower() == 'y':
            total_resources += explore_planet()
        else:
            break

        total_damage += encounter_asteroid()
        total_damage += encounter_enemy()

        print("Total resources collected: " + str(total_resources))
        print("Total damage taken: " + str(total_damage))
        print()
    
    print("Thanks for playing Space Explorer!")

if __name__ == "__main__":
    main()

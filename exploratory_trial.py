
import random

def explore_planet():
    planet = random.choice(["Mars", "Neptune", "Jupiter", "Saturn", "Mercury"])
    print("Exploring planet:", planet)
    resources = random.randint(1, 10)
    print("Gathered resources:", resources)
    return resources

def space_adventure():
    total_resources = 0
    while True:
        decision = input("Do you want to explore a new planet? (yes/no): ")
        if decision.lower() == "yes":
            resources = explore_planet()
            total_resources += resources
            print("Total resources gathered so far:", total_resources)
        else:
            print("Thanks for playing!")
            break

space_adventure()

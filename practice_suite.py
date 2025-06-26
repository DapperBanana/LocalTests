
import random

def explore():
    planets = ["Earth", "Mars", "Jupiter", "Saturn", "Neptune"]
    alien_encounter = random.choice([True, False])

    print("Welcome to the space exploration game! Your mission is to explore new planets.")
    print("You are now traveling through space...")
    print("You have arrived at a new planet!")

    current_planet = random.choice(planets)
    print("You have landed on {}".format(current_planet))

    if alien_encounter:
        print("Oh no! You have encountered hostile aliens on this planet. You must fight to survive!")
        fight = random.choice([True, False])
        if fight:
            print("You have defeated the aliens and can continue your exploration.")
        else:
            print("You were overpowered by the aliens. Game over.")
            return

    print("You have successfully explored {}! Would you like to continue exploring? (yes/no)".format(current_planet))
    choice = input().lower()
    
    if choice == "yes":
        explore()
    else:
        print("Thanks for playing!")

explore()

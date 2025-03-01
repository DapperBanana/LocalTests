
import random
import time

def explore():
    print("You are on a mission to explore outer space.")
    print("Your spaceship is equipped with everything you need to survive.")
    print("You have limited fuel and oxygen, so choose your actions wisely.")

    fuel = 100
    oxygen = 100

    while True:
        print("\nFuel: {}% | Oxygen: {}%".format(fuel, oxygen))
        print("What would you like to do?")
        print("1. Search for resources")
        print("2. Visit a nearby planet")
        print("3. Return to Earth")

        choice = input("Enter your choice: ")

        if choice == "1":
            resources = random.randint(1, 20)
            fuel -= 5
            oxygen -= 5
            print("You found {} resources but used up some fuel and oxygen.".format(resources))

        elif choice == "2":
            planet = random.choice(["Mars", "Jupiter", "Saturn", "Neptune"])
            fuel -= 20
            oxygen -= 20
            print("You visited {} but it was too dangerous to land.".format(planet))

        elif choice == "3":
            print("You safely returned to Earth.")
            break

        if fuel <= 0 or oxygen <= 0:
            print("You ran out of fuel or oxygen and died in space.")
            break

        time.sleep(1)

explore()

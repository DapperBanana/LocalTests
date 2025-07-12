
import random

def explore():
    print("You are now exploring space...")
    while True:
        choice = input("Do you want to (1) continue exploring or (2) return to Earth? ")
        if choice == "1":
            explore_result = random.choice(["You discovered a new planet!", "You found a rare space relic!", "You encountered an alien civilization!"])
            print(explore_result)
        elif choice == "2":
            print("You are returning to Earth...")
            break
        else:
            print("Invalid input, please try again.")

explore()

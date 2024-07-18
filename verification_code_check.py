
import random

def explore():
    print("You are in the spaceship heading to an unknown planet...")
    while True:
        choice = input("Do you want to continue exploring? (y/n): ")
        if choice.lower() == 'y':
            print("You encounter an alien civilization.")
            decision = input("Do you want to interact with them? (y/n): ")
            if decision.lower() == 'y':
                print("The aliens are friendly and offer you valuable resources.")
            else:
                print("The aliens seem hostile and attack your spaceship.")
                print("Game over.")
                break
        else:
            print("You decide to return to Earth.")
            print("Congratulations, you have successfully completed your space exploration mission!")
            break

explore()

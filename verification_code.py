
import random

def explore_planet():
    print("Welcome to the Space Exploration Game!")
    print("You are about to embark on a journey to explore a new planet.")
    print("You land on the planet and see two paths in front of you: Path 1 and Path 2.")
    choice = input("Which path will you choose? (1/2): ")

    if choice == "1":
        encounter1()
    elif choice == "2":
        encounter2()
    else:
        print("Invalid choice. Please choose again.")
        explore_planet()

def encounter1():
    print("You chose Path 1 and encounter an alien creature!")
    print("It demands to see your spaceship key. What will you do?")
    choice = input("Give key / Run away: ")

    if choice.lower() == "give key":
        print("The alien takes your key and lets you pass safely.")
        print("You continue exploring the planet.")
    elif choice.lower() == "run away":
        print("You try to run away, but the alien catches you.")
        print("Game over! Better luck next time.")
    else:
        print("Invalid choice. Please choose again.")
        encounter1()

def encounter2():
    print("You chose Path 2 and find a treasure chest!")
    print("You can either open it or leave it behind. What will you do?")
    choice = input("Open chest / Leave chest: ")

    if choice.lower() == "open chest":
        print("You found valuable resources inside the chest.")
        print("Congratulations, you have completed your mission!")
    elif choice.lower() == "leave chest":
        print("You leave the chest behind and continue exploring the planet.")
        print("You encounter some challenges but successfully complete your mission.")
    else:
        print("Invalid choice. Please choose again.")
        encounter2()

explore_planet()

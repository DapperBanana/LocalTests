
import random

def explore():
    print("You are in a spaceship, ready to embark on a space exploration mission.")
    print("You can choose to explore different planets or galaxies.")
    
    choices = ["Mars", "Jupiter", "Saturn", "Galaxy1", "Galaxy2"]
    choice = random.choice(choices)
    
    print("You have arrived at", choice)
    
    if choice == "Mars":
        print("You have found evidence of past life on Mars. Do you want to continue exploring?")
        response = input("Enter 'yes' to continue or 'no' to return to Earth: ")
        
        if response == "yes":
            print("You continue exploring Mars and discover a hidden underground cave.")
        else:
            print("You return to Earth.")
    
    elif choice == "Jupiter":
        print("You have encountered a massive storm on Jupiter. Do you want to continue exploring?")
        response = input("Enter 'yes' to continue or 'no' to return to Earth: ")
        
        if response == "yes":
            print("You navigate through the storm and find an ancient alien artifact.")
        else:
            print("You return to Earth.")
    
    elif choice == "Saturn":
        print("You have discovered a ring of debris around Saturn. Do you want to continue exploring?")
        response = input("Enter 'yes' to continue or 'no' to return to Earth: ")
        
        if response == "yes":
            print("You analyze the debris and find remnants of an ancient spaceship.")
        else:
            print("You return to Earth.")
    
    elif choice == "Galaxy1":
        print("You have entered an unknown galaxy. Do you want to continue exploring?")
        response = input("Enter 'yes' to continue or 'no' to return to Earth: ")
        
        if response == "yes":
            print("You encounter a hostile alien race and narrowly escape.")
        else:
            print("You return to Earth.")
    
    else:
        print("You have discovered a galaxy with multiple habitable planets. Do you want to continue exploring?")
        response = input("Enter 'yes' to continue or 'no' to return to Earth: ")
        
        if response == "yes":
            print("You find a planet with advanced civilization willing to make contact with Earth.")
        else:
            print("You return to Earth.")

explore()

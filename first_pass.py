
import random

def explore_planet():
    print("You have reached a new planet!")
    decision = input("Do you want to explore it? (yes/no): ")
    
    if decision.lower() == "yes":
        resources = random.randint(1, 10)
        print(f"You have found {resources} resources on this planet.")
    else:
        print("You decide to move on to the next planet.")

def main():
    print("Welcome to the Space Exploration Game!")
    
    while True:
        choice = input("Do you want to explore a new planet? (yes/no): ")
        
        if choice.lower() == "yes":
            explore_planet()
        else:
            print("Thank you for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()

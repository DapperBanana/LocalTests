
import random

def explore():
    print("Welcome to the Space Exploration Game!")
    print("You are an astronaut exploring a distant planet.")
    
    while True:
        choice = input("Do you want to [1] explore the planet or [2] return to Earth? ")
        
        if choice == '1':
            print("You decide to explore the planet...")
            explore_planet()
        elif choice == '2':
            print("You decide to return to Earth. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def explore_planet():
    resources = 100
    days = 0
    
    while resources > 0:
        days += 1
        print("\nDay", days)
        print("Resources remaining:", resources)
        
        action = input("[1] Gather resources [2] Rest [3] Return to Earth: ")
        
        if action == '1':
            gathered = random.randint(1, 20)
            resources += gathered
            print("You gather", gathered, "resources.")
        elif action == '2':
            resources -= 10
            print("You rest and recover some resources.")
        elif action == '3':
            print("You decide to return to Earth. Goodbye!")
            break
        else:
            print("Invalid action. Please try again.")
        
        if resources <= 0:
            print("You have run out of resources. Game over!")
            break

explore()

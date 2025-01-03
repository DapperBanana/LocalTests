
import random

def explore():
    print("You are on a mission to explore outer space.")
    print("You can choose to travel to different planets or engage in other activities.")

    while True:
        print("\nOptions:")
        print("1. Travel to a new planet")
        print("2. Collect resources")
        print("3. Explore a moon")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            planet = random.choice(['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'])
            print(f"Traveling to {planet}...")
            print(f"You have reached {planet}!")
        
        elif choice == '2':
            print("Collecting resources...")
            resources = random.randint(1, 10)
            print(f"You have collected {resources} resources.")
        
        elif choice == '3':
            moon = random.choice(['Io', 'Titan', 'Europa', 'Ganymede'])
            print(f"You are exploring {moon}.")
            print("You find some interesting features on the moon.")

        elif choice == '4':
            print("Thanks for playing. See you next time!")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

explore()

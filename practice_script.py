
import random

def explore():
    print("You are on a space exploration mission.")
    print("You have landed on a new planet.")
    
    choices = ["Explore the planet", "Collect samples", "Analyze data", "Head back to your ship"]
    
    while True:
        print("\nWhat would you like to do?")
        
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        
        action = input("Enter the number of your choice: ")
        
        if action == "1":
            explore_planet()
        elif action == "2":
            collect_samples()
        elif action == "3":
            analyze_data()
        elif action == "4":
            return
        else:
            print("Invalid choice. Please try again.")

def explore_planet():
    print("You are exploring the planet.")
    print("You come across a strange alien artifact.")
    
    artifact = random.choice(["a glowing crystal", "a mysterious orb", "a metallic cube"])
    
    print(f"You found {artifact}. What do you do?")
    
    action = input("Take it with you? (y/n): ")
    
    if action.lower() == "y":
        print(f"You took {artifact} with you.")
    else:
        print("You left the artifact behind.")
    
def collect_samples():
    print("You are collecting samples from the planet.")
    print("You find some interesting rock formations.")
    
    analysis = random.choice(["The rocks contain rare minerals", "The rocks are fossilized alien remains", "The rocks emit strange energy"])
    
    print(f"{analysis}.")
    
def analyze_data():
    print("You are analyzing the data collected on the planet.")
    print("You discover a pattern in the weather system.")
    
    pattern = random.choice(["The planet is experiencing a long drought", "A storm is approaching", "An eclipse is imminent"])
    
    print(f"{pattern}.")
    
explore()

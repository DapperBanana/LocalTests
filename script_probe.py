
import random

def explore():
    print("You are now on a space exploration mission!")
    print("You can choose to explore different planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune")
    
    while True:
        choice = input("Which planet do you want to explore? ").lower()
        
        if choice in ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]:
            print(f"You are now exploring {choice.capitalize()}...")
            print("You encounter...")
            encounter = random.choice(["an alien civilization", "a toxic atmosphere", "unusual plant life", "an asteroid field", "a mysterious artifact"])
            print(encounter)
            play_again = input("Do you want to explore another planet? (yes/no) ").lower()
            if play_again != "yes":
                break
        else:
            print("Invalid planet choice. Please choose from the list.")
            

explore()

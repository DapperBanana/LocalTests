
import random

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 10)
        self.happiness = random.randint(0, 10)
    
    def feed(self):
        self.hunger -= 1
        print(f"{self.name} has been fed!")
    
    def play(self):
        self.happiness += 1
        print(f"{self.name} is happy after playing!")

    def status(self):
        print(f"{self.name}'s hunger level: {self.hunger}")
        print(f"{self.name}'s happiness level: {self.happiness}")

pet_name = input("Enter a name for your virtual pet: ")
pet = VirtualPet(pet_name)

while True:
    action = input("Enter an action (feed, play, status, quit): ").lower()
    
    if action == "feed":
        pet.feed()
    elif action == "play":
        pet.play()
    elif action == "status":
        pet.status()
    elif action == "quit":
        print("Goodbye!")
        break
    else:
        print("Invalid action. Try again.")

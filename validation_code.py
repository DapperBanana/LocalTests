
import random

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 10)
        self.energy = random.randint(0, 10)
        self.happiness = random.randint(0, 10)

    def feed(self):
        self.hunger -= 2
        if self.hunger < 0:
            self.hunger = 0
        self.energy += 1
        self.happiness += 1

    def play(self):
        self.energy -= 2
        if self.energy < 0:
            self.energy = 0
        self.happiness += 2

    def pet(self):
        self.happiness += 1

    def status(self):
        print(f"{self.name}'s stats:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

pet_name = input("Enter a name for your virtual pet: ")
pet = VirtualPet(pet_name)

while True:
    pet.status()

    action = input("What would you like to do? (feed/play/pet/quit): ")
    
    if action == 'feed':
        pet.feed()
    elif action == 'play':
        pet.play()
    elif action == 'pet':
        pet.pet()
    elif action == 'quit':
        break
    else:
        print("Invalid action. Try again.")

    print()

print("Goodbye! Thanks for playing with your virtual pet.")

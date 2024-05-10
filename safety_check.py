
import random

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 10)
        self.happiness = random.randint(0, 10)
    
    def feed(self):
        self.hunger -= 2
        self.happiness += 1
    
    def play(self):
        self.hunger += 1
        self.happiness += 2
    
    def __str__(self):
        return f"{self.name} - Hunger: {self.hunger}, Happiness: {self.happiness}"

pet_name = input("Enter a name for your virtual pet: ")
pet = VirtualPet(pet_name)

while True:
    print("\n" + str(pet))
    print("1. Feed")
    print("2. Play")
    print("3. Quit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        pet.feed()
    elif choice == "2":
        pet.play()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

print("Thanks for playing with your virtual pet!")

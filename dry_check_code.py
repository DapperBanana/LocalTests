
import random

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 10)
        self.happiness = random.randint(0, 10)
    
    def feed(self):
        self.hunger -= 2
        print(f"{self.name} has been fed!")
    
    def play(self):
        self.hunger += 1
        self.happiness += 2
        print(f"{self.name} is happy playing!")
    
    def check_status(self):
        print(f"{self.name}'s hunger level: {self.hunger}")
        print(f"{self.name}'s happiness level: {self.happiness}")

# Main program
print("Welcome to the virtual pet simulator!")
pet_name = input("Enter the name of your pet: ")
pet = VirtualPet(pet_name)

while True:
    print("\nWhat would you like to do?")
    print("1. Feed pet")
    print("2. Play with pet")
    print("3. Check pet's status")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        pet.feed()
    elif choice == '2':
        pet.play()
    elif choice == '3':
        pet.check_status()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")

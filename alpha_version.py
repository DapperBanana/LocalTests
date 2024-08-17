
import random

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 10)
        self.energy = random.randint(0, 10)
    
    def feed(self):
        self.hunger -= random.randint(1, 3)
        if self.hunger < 0:
            self.hunger = 0
    
    def play(self):
        self.energy -= random.randint(1, 3)
        if self.energy < 0:
            self.energy = 0
    
    def status(self):
        print(f"{self.name}'s Hunger: {self.hunger}")
        print(f"{self.name}'s Energy: {self.energy}")
    
def main():
    pet_name = input("Enter a name for your virtual pet: ")
    pet = VirtualPet(pet_name)
    
    while True:
        print("\nWhat would you like to do with your pet?")
        print("1. Feed")
        print("2. Play")
        print("3. Check status")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.status()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()

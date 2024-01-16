
import random

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 10)
        self.boredom = random.randint(0, 10)
    
    def __str__(self):
        return f"{self.name}: Hunger: {self.hunger}, Boredom: {self.boredom}"
    
    def feed(self):
        self.hunger -= random.randint(1, 3)
        self.hunger = max(0, self.hunger)
        self.boredom += random.randint(0, 2)
        self.boredom = min(10, self.boredom)
    
    def play(self):
        self.boredom -= random.randint(1, 3)
        self.boredom = max(0, self.boredom)
        self.hunger += random.randint(0, 2)
        self.hunger = min(10, self.hunger)

def main():
    pet_name = input("Enter a name for your pet: ")
    pet = VirtualPet(pet_name)
    
    while True:
        print(pet)
        choice = input("What would you like to do? (feed/play/quit): ")
        
        if choice == "feed":
            pet.feed()
        elif choice == "play":
            pet.play()
        elif choice == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
        
        print()
    
if __name__ == "__main__":
    main()

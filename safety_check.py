
import random

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(1, 10)
        self.happiness = random.randint(1, 10)
        self.energy = random.randint(1, 10)

    def feed(self):
        self.hunger -= random.randint(1, 3)
        if self.hunger < 0:
            self.hunger = 0
        self.happiness += random.randint(1, 2)
        self.energy -= 1

    def play(self):
        self.hunger += random.randint(1, 2)
        self.happiness += random.randint(1, 3)
        self.energy -= random.randint(1, 2)

    def sleep(self):
        self.energy += random.randint(1, 3)

    def status(self):
        print(f"{self.name}'s stats:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}")

# Main program
pet_name = input("Enter the name of your virtual pet: ")
pet = VirtualPet(pet_name)

while True:
    pet.status()
    choice = input("What would you like to do? (feed/play/sleep/quit): ")

    if choice == 'feed':
        pet.feed()
    elif choice == 'play':
        pet.play()
    elif choice == 'sleep':
        pet.sleep()
    elif choice == 'quit':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

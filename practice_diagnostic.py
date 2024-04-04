
class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        self.hunger -= 10
        self.happiness += 10

    def play(self):
        self.hunger += 10
        self.happiness += 20

    def status(self):
        print(f"{self.name} - Hunger: {self.hunger}, Happiness: {self.happiness}")

# Main code
pet_name = input("Enter the name of your virtual pet: ")
pet = VirtualPet(pet_name)

while True:
    choice = input("Enter 'feed', 'play', or 'quit': ")

    if choice == "feed":
        pet.feed()
    elif choice == "play":
        pet.play()
    elif choice == "quit":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

    pet.status()

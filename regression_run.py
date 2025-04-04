
class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        self.hunger -= 10
        self.happiness += 5
        print(f"{self.name} has been fed.")

    def play(self):
        self.hunger += 5
        self.happiness += 10
        print(f"{self.name} is happy playing.")

    def check_status(self):
        print(f"{self.name} Hunger level: {self.hunger}")
        print(f"{self.name} Happiness level: {self.happiness}")

# Main program
pet_name = input("Enter the name of your virtual pet: ")
pet = VirtualPet(pet_name)

while True:
    choice = input("What do you want to do? (feed, play, check, quit): ")

    if choice == 'feed':
        pet.feed()
    elif choice == 'play':
        pet.play()
    elif choice == 'check':
        pet.check_status()
    elif choice == 'quit':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

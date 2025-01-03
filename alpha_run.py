
class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happiness = 10

    def feed(self):
        self.hunger -= 1

    def play(self):
        self.happiness += 1

    def check_status(self):
        print(f"{self.name}'s hunger level: {self.hunger}")
        print(f"{self.name}'s happiness level: {self.happiness}")

# Main program
pet_name = input("Enter the name of your virtual pet: ")
pet = VirtualPet(pet_name)

while True:
    action = input("Enter an action (feed, play, status, or exit): ")

    if action == "feed":
        pet.feed()
        print(f"{pet.name} has been fed.")
    elif action == "play":
        pet.play()
        print(f"{pet.name} is happy!")
    elif action == "status":
        pet.check_status()
    elif action == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid action. Please try again.")

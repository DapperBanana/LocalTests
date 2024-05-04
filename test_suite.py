
class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        self.hunger -= 10
        self.happiness += 5

    def play(self):
        self.happiness += 10
        self.hunger += 5

    def check_status(self):
        print(f'{self.name}\'s hunger level: {self.hunger}')
        print(f'{self.name}\'s happiness level: {self.happiness}')

pet_name = input("Enter your pet's name: ")
pet = VirtualPet(pet_name)

while True:
    print("\n1. Feed your pet")
    print("2. Play with your pet")
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
        print("Invalid choice. Please try again.")

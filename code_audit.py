
class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        self.hunger -= 10
        print(f"{self.name} is fed and hunger level decreased by 10.")

    def play(self):
        self.happiness += 10
        print(f"{self.name} is played with and happiness level increased by 10.")

    def status(self):
        print(f"{self.name}'s hunger level: {self.hunger}")
        print(f"{self.name}'s happiness level: {self.happiness}")


pet_name = input("Enter a name for your virtual pet: ")
pet = VirtualPet(pet_name)

while True:
    print("\nVirtual Pet Menu:")
    print("1. Feed Pet")
    print("2. Play with Pet")
    print("3. Check status")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        pet.feed()
    elif choice == '2':
        pet.play()
    elif choice == '3':
        pet.status()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please choose again.")

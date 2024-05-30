
class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.happiness = 5
        self.hunger = 5
        self.energy = 5

    def feed(self):
        self.hunger -= 1
        if self.hunger < 0:
            self.hunger = 0
        self.happiness += 1

    def play(self):
        self.energy -= 1
        if self.energy < 0:
            self.energy = 0
        self.happiness += 1

    def sleep(self):
        self.energy += 2
        if self.energy > 5:
            self.energy = 5

    def status(self):
        print(f"{self.name}:")
        print(f"Happiness: {self.happiness}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")

# Main code
def main():
    name = input("Enter the name of your virtual pet: ")
    pet = VirtualPet(name)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Check status")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            pet.status()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

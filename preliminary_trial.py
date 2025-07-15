
import time

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        self.hunger -= 10
        print(f"{self.name} has been fed!")

    def play(self):
        self.happiness += 10
        print(f"{self.name} is happy!")

    def check_status(self):
        print(f"{self.name}'s hunger level: {self.hunger}")
        print(f"{self.name}'s happiness level: {self.happiness}")

    def update(self):
        self.hunger += 5
        self.happiness -= 5

def main():
    name = input("Enter a name for your virtual pet: ")
    pet = VirtualPet(name)

    while True:
        pet.update()
        print("\nWhat would you like to do?")
        print("1. Feed pet")
        print("2. Play with pet")
        print("3. Check pet's status")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.check_status()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        time.sleep(1)

if __name__ == "__main__":
    main()

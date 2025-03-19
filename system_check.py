
import time
import random

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        self.hunger -= 10
        print(f"{self.name} has been fed.")
    
    def play(self):
        self.happiness += 10
        print(f"{self.name} is happy.")

    def check_status(self):
        print(f"{self.name}'s hunger level is {self.hunger}")
        print(f"{self.name}'s happiness level is {self.happiness}")

def main():
    pet_name = input("Enter a name for your virtual pet: ")
    pet = VirtualPet(pet_name)

    while pet.hunger > 0 and pet.happiness < 100:
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Check status")
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

        pet.hunger += random.randint(0, 10)
        pet.happiness -= random.randint(0, 10)
        
        time.sleep(1)

if __name__ == "__main__":
    main()

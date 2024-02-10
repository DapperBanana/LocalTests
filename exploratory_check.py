
import random

# Spaceship class
class Spaceship:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.fuel = 100
        self.location = random.randint(1, 5)
    
    def move(self):
        if self.fuel <= 0:
            print("Not enough fuel to move!")
            return
        
        new_location = random.randint(1, 5)
        self.location = new_location
        self.fuel -= 10
        
        print(f"{self.name} has moved to location {self.location}.")
        print(f"Fuel remaining: {self.fuel}")
    
    def refuel(self):
        self.fuel = 100
        print("Spaceship refueled!")
    
    def repair(self):
        self.health = 100
        print("Spaceship repaired!")
    
    def status(self):
        print(f"Spaceship Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Fuel: {self.fuel}")
        print(f"Location: {self.location}")


# Game loop
def game():
    spaceship_name = input("Enter spaceship name: ")
    spaceship = Spaceship(spaceship_name)
    
    while True:
        print("\nEnter a command:")
        print("1 -> Status")
        print("2 -> Move")
        print("3 -> Refuel")
        print("4 -> Repair")
        print("5 -> Quit")
        
        choice = input()
        
        if choice == "1":
            spaceship.status()
        elif choice == "2":
            spaceship.move()
        elif choice == "3":
            spaceship.refuel()
        elif choice == "4":
            spaceship.repair()
        elif choice == "5":
            print("\nGame Over!")
            break
        else:
            print("Invalid choice, try again!")


# Start the game
game()

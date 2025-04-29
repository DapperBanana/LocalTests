
import time
import random

class Spaceship:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.fuel = 100
        self.weapon = "Laser Blaster"
    
    def status(self):
        print(f"{self.name} Status:")
        print(f"Health: {self.health}")
        print(f"Fuel: {self.fuel}")
        print(f"Weapon: {self.weapon}")

    def attack(self):
        print(f"{self.name} attacks with {self.weapon}!")
        damage = random.randint(10, 20)
        return damage

    def refuel(self):
        print(f"Refueling {self.name}...")
        self.fuel = 100

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage!")

player_ship = Spaceship("Player Ship")
enemy_ship = Spaceship("Enemy Ship")

while player_ship.health > 0 and enemy_ship.health > 0:
    player_ship.status()
    enemy_ship.status()

    choice = input("Enter 'a' to attack, 'r' to refuel, or 'q' to quit: ")
    
    if choice == 'a':
        enemy_damage = player_ship.attack()
        enemy_ship.take_damage(enemy_damage)
    elif choice == 'r':
        player_ship.refuel()
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Try again.")

    enemy_damage = enemy_ship.attack()
    player_ship.take_damage(enemy_damage)

    time.sleep(1)

if player_ship.health <= 0:
    print("Game over. You lose.")
elif enemy_ship.health <= 0:
    print("Congratulations! You defeated the enemy.")

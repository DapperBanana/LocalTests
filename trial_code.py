
import random

class Spaceship:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.shield = 50
        self.weapon = "Laser"
    
    def attack(self):
        damage = random.randint(10, 20)
        return damage
    
    def take_damage(self, damage):
        if self.shield > 0:
            self.shield -= damage
        else:
            self.health -= damage
    
    def status(self):
        print(f"{self.name} Status:\nHealth: {self.health}\nShield: {self.shield}\n")
        
player_name = input("Enter your spaceship name: ")
player_ship = Spaceship(player_name)

enemy_ship = Spaceship("Enemy")

while player_ship.health > 0 and enemy_ship.health > 0:
    player_ship.status()
    enemy_ship.status()
    
    print("1. Attack")
    print("2. Escape")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        enemy_damage = player_ship.attack()
        enemy_ship.take_damage(enemy_damage)
        print(f"You attacked {enemy_ship.name} for {enemy_damage} damage!")
        
        player_damage = enemy_ship.attack()
        player_ship.take_damage(player_damage)
        print(f"{enemy_ship.name} attacked you for {player_damage} damage!")
    
    elif choice == '2':
        print("You escaped the battle!")
        break
    
    if player_ship.health <= 0:
        print("Game Over. Your spaceship was destroyed!")
    elif enemy_ship.health <= 0:
        print("Congratulations! You defeated the enemy spaceship!")



import random

# Define player class
class Player:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack_enemy(self):
        return random.randint(1, self.attack)

# Define enemy class
class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack_player(self):
        return random.randint(1, self.attack)

# Game logic
def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while player.is_alive() and enemy.is_alive():
        player_damage = player.attack_enemy()
        enemy_damage = enemy.attack_player()

        print(f"{player.name} attacks {enemy.name} for {player_damage} damage")
        enemy.take_damage(player_damage)

        print(f"{enemy.name} attacks {player.name} for {enemy_damage} damage")
        player.take_damage(enemy_damage)

        print(f"{player.name} health: {player.health}")
        print(f"{enemy.name} health: {enemy.health}")
        print("")

    if player.is_alive():
        print(f"{player.name} defeated {enemy.name}!")
    else:
        print(f"{player.name} was defeated by {enemy.name}!")

# Initialize player and enemy
player = Player("Hero", 100, 10)
enemy = Enemy("Goblin", 50, 5)

# Start the game
battle(player, enemy)

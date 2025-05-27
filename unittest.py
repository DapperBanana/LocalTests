
import random

class Player:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0

def battle(player, enemy):
    while player.is_alive() and enemy.is_alive():
        player_damage = random.randint(1, player.attack)
        enemy_damage = random.randint(1, enemy.attack)

        print(f"{player.name} attacks {enemy.name} for {player_damage} damage.")
        enemy.take_damage(player_damage)

        print(f"{enemy.name} attacks {player.name} for {enemy_damage} damage.")
        player.take_damage(enemy_damage)

        print(f"{player.name} HP: {player.hp}")
        print(f"{enemy.name} HP: {enemy.hp}")
        print("")

    if player.is_alive():
        print(f"{player.name} wins!")
    else:
        print(f"{enemy.name} wins!")

# Create player and enemy
player = Player("Hero", 100, 10)
enemy = Enemy("Dragon", 50, 20)

# Start battle
battle(player, enemy)

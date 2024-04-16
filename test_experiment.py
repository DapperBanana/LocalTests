
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.defense = 5

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
        player_damage = max(0, random.randint(0, player.attack) - enemy.attack)
        enemy_damage = max(0, random.randint(0, enemy.attack) - player.defense)

        player.take_damage(enemy_damage)
        enemy.take_damage(player_damage)

        print(f"{enemy.name} attacks {player.name} for {enemy_damage} damage")
        print(f"{player.name} attacks {enemy.name} for {player_damage} damage")

    if player.is_alive():
        print(f"{player.name} wins!")
    else:
        print(f"{enemy.name} wins!")

player_name = input("Enter your name: ")
player = Player(player_name)

goblin = Enemy("Goblin", 50, 5)

print("A wild goblin appears! It's time to battle!")
battle(player, goblin)

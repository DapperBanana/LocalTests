
import random

class Player:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack(self):
        return random.randint(1, self.atk)

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0

class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack(self):
        return random.randint(1, self.atk)

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0

def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")
    
    while player.is_alive() and enemy.is_alive():
        player_damage = player.attack()
        enemy_damage = enemy.attack()

        print(f"{player.name} attacks {enemy.name} for {player_damage} damage!")
        enemy.take_damage(player_damage)
        
        if not enemy.is_alive():
            print(f"{enemy.name} has been defeated!")
            break

        print(f"{enemy.name} attacks {player.name} for {enemy_damage} damage!")
        player.take_damage(enemy_damage)

        if not player.is_alive():
            print(f"{player.name} has been defeated!")
            break

    return player.is_alive()

player = Player("Hero", 100, 10)
enemy = Enemy("Goblin", 50, 5)

result = battle(player, enemy)

if result:
    print("You win!")
else:
    print("Game over")


import random

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack_power = 10

    def attack(self):
        return random.randint(1, self.attack_power)

# Enemy class
class Enemy:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self):
        return random.randint(1, self.attack_power)

# Battle function
def battle(player, enemy):
    print(f"{player.name} vs {enemy.name}!")
    while player.hp > 0 and enemy.hp > 0:
        player_damage = player.attack()
        enemy_damage = enemy.attack()

        print(f"{player.name} attacks {enemy.name} for {player_damage} damage!")
        enemy.hp -= player_damage
        print(f"{enemy.name} has {enemy.hp} HP left.")

        if enemy.hp <= 0:
            print(f"{player.name} wins!")
            break

        print(f"{enemy.name} attacks {player.name} for {enemy_damage} damage!")
        player.hp -= enemy_damage
        print(f"{player.name} has {player.hp} HP left.")

        if player.hp <= 0:
            print(f"{enemy.name} wins!")
            break

# Main program
player = Player("Player")
enemy = Enemy("Enemy", 50, 5)

battle(player, enemy)

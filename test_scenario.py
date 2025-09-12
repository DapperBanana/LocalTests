
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

    def attack_enemy(self):
        return random.randint(1, self.attack)

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0

    def attack_player(self):
        return random.randint(1, self.attack)

def battle(player, enemy):
    print("A wild {} appears!".format(enemy.name))

    while player.is_alive() and enemy.is_alive():
        player_damage = player.attack_enemy()
        enemy_damage = enemy.attack_player()

        print("{} attacks for {} damage.".format(player.name, player_damage))
        enemy.take_damage(player_damage)

        if not enemy.is_alive():
            print("The enemy {} has been defeated!".format(enemy.name))
            break

        print("{} attacks for {} damage.".format(enemy.name, enemy_damage))
        player.take_damage(enemy_damage)

        if not player.is_alive():
            print("Game over. You have been defeated by the enemy {}.".format(enemy.name))
            break

player = Player("Hero", 100, 10)
enemy = Enemy("Goblin", 50, 5)

battle(player, enemy)

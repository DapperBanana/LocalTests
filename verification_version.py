
import random

class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def take_damage(self, damage):
        self.health -= damage
        
    def is_alive(self):
        return self.health > 0
        
    def attack(self):
        return random.randint(1, self.attack_power)

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def take_damage(self, damage):
        self.health -= damage
        
    def is_alive(self):
        return self.health > 0
        
    def attack(self):
        return random.randint(1, self.attack_power)

def battle(player, enemy):
    print("A wild {} appears! Get ready to battle!".format(enemy.name))
    
    while player.is_alive() and enemy.is_alive():
        player_damage = player.attack()
        enemy_damage = enemy.attack()
        
        print("{} attacks {} for {} damage.".format(player.name, enemy.name, player_damage))
        enemy.take_damage(player_damage)
        
        if not enemy.is_alive():
            print("{} defeats {}! Victory!".format(player.name, enemy.name))
            break
        
        print("{} attacks {} for {} damage.".format(enemy.name, player.name, enemy_damage))
        player.take_damage(enemy_damage)
        
        if not player.is_alive():
            print("{} has been defeated by {}! Game over.".format(player.name, enemy.name))
            break
        
player = Player("Hero", 100, 20)
enemy = Enemy("Goblin", 50, 10)

battle(player, enemy)

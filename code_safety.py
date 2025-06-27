
import random

class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.attack = 10
        self.defense = 5
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        actual_damage = max(damage - self.defense, 0)
        self.health -= actual_damage
        print(f"{self.name} takes {actual_damage} damage.")
    
    def attack_enemy(self):
        return self.attack + random.randint(-3, 3)

class Enemy:
    def __init__(self, name, health=50):
        self.name = name
        self.health = health
        self.attack = 8
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage.")
    
    def attack_player(self):
        return self.attack + random.randint(-2, 2)

def combat(player, enemy):
    while player.is_alive() and enemy.is_alive():
        player_damage = player.attack_enemy()
        enemy_damage = enemy.attack_player()
        
        enemy.take_damage(player_damage)
        if not enemy.is_alive():
            print(f"{enemy.name} has been defeated!")
            break
        
        player.take_damage(enemy_damage)
        if not player.is_alive():
            print(f"{player.name} has been defeated.")
            break

def main():
    player = Player("Player1")
    enemy1 = Enemy("Goblin1")
    enemy2 = Enemy("Dragon1")
    
    print("A wild enemy appears! ")
    combat(player, enemy1)
    
    print("\nAnother enemy approaches! ")
    combat(player, enemy2)

if __name__ == "__main__":
    main()


import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.defense = 5
    
    def take_damage(self, damage):
        self.hp -= max(0, damage - self.defense)
    
    def attack_enemy(self):
        return random.randint(1, self.attack)

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    
    def take_damage(self, damage):
        self.hp -= max(0, damage)
    
    def attack_player(self):
        return random.randint(1, self.attack)

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    enemy = Enemy("Dragon", 50, 15)
    
    print(f"Welcome, {player.name}! Can you defeat the mighty Dragon?")
    
    while player.hp > 0 and enemy.hp > 0:
        player_damage = player.attack_enemy()
        enemy_damage = enemy.attack_player()
        
        print(f"{player.name} attacks the {enemy.name} for {player_damage} damage.")
        enemy.take_damage(player_damage)
        
        print(f"The {enemy.name} attacks {player.name} for {enemy_damage} damage.")
        player.take_damage(enemy_damage)
        
        print(f"{player.name}'s HP: {player.hp}")
        print(f"{enemy.name}'s HP: {enemy.hp}")
        print()
    
    if player.hp <= 0:
        print("You have been defeated! Game Over.")
    else:
        print(f"Congratulations, {player.name}! You have defeated the {enemy.name}.")

if __name__ == "__main__":
    main()

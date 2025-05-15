
import random

player_hp = 100
enemy_hp = 50
player_attack = 10
enemy_attack = 5

def battle():
    global player_hp, enemy_hp
    
    while player_hp > 0 and enemy_hp > 0:
        player_damage = random.randint(1, player_attack)
        enemy_damage = random.randint(1, enemy_attack)
        
        print(f"Player attacks for {player_damage} damage!")
        enemy_hp -= player_damage
        print(f"Enemy HP: {enemy_hp}")
        
        if enemy_hp <= 0:
            print("Enemy defeated!")
            break
        
        print(f"Enemy attacks for {enemy_damage} damage!")
        player_hp -= enemy_damage
        print(f"Player HP: {player_hp}")
        
        if player_hp <= 0:
            print("Player has been defeated!")
            break

battle()


import random

player_health = 100
enemy_health = 100

def player_attack():
    return random.randint(10, 20)

def enemy_attack():
    return random.randint(5, 15)

while player_health > 0 and enemy_health > 0:
    print("Player Health: ", player_health)
    print("Enemy Health: ", enemy_health)
    
    player_damage = player_attack()
    enemy_damage = enemy_attack()
    
    print("Player attacks for", player_damage, "damage.")
    enemy_health -= player_damage
    
    if enemy_health <= 0:
        print("Enemy defeated! You win!")
        break
    
    print("Enemy attacks for", enemy_damage, "damage.")
    player_health -= enemy_damage
    
    if player_health <= 0:
        print("Player defeated! Game over.")
        break

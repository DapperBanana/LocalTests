
import random

player_health = 100
enemy_health = 50

def print_status():
    print("Player Health:", player_health)
    print("Enemy Health:", enemy_health)
    print()

def player_attack():
    damage = random.randint(5, 15)
    print("You attack the enemy for", damage, "damage.")
    return damage

def enemy_attack():
    damage = random.randint(3, 10)
    print("The enemy attacks you for", damage, "damage.")
    return damage

while player_health > 0 and enemy_health > 0:
    print_status()
    
    player_damage = player_attack()
    enemy_health -= player_damage
    
    if enemy_health <= 0:
        print("You defeated the enemy!")
        break
        
    enemy_damage = enemy_attack()
    player_health -= enemy_damage
    
    if player_health <= 0:
        print("You were defeated by the enemy.")
        break

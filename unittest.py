
import random

player_health = 100
player_attack = 10
player_defense = 5

enemy_health = random.randint(50, 100)
enemy_attack = random.randint(5, 15)
enemy_defense = random.randint(1, 5)

def battle():
    global player_health, enemy_health
    
    while player_health > 0 and enemy_health > 0:
        player_damage = max(0, player_attack - enemy_defense)
        enemy_damage = max(0, enemy_attack - player_defense)
        
        enemy_health -= player_damage
        player_health -= enemy_damage
        
        print(f"Player health: {player_health}")
        print(f"Enemy health: {enemy_health}")
        
        if enemy_health <= 0:
            print("You defeated the enemy!")
        elif player_health <= 0:
            print("You were defeated!")
        else:
            command = input("Attack or defend? (a/d): ")
            if command == "a":
                print("You attack the enemy!")
            elif command == "d":
                print("You defend against the enemy's attack!")
            else:
                print("Invalid command, please try again.")

battle()


import random

player_health = 100
enemy_health = 100

def attack(attacker, defender):
    damage = random.randint(5, 15)
    defender -= damage
    return defender, damage

def battle():
    global player_health, enemy_health

    while player_health > 0 and enemy_health > 0:
        print("Player health: ", player_health)
        print("Enemy health: ", enemy_health)
        print("1. Attack")
        print("2. Run")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            enemy_health, damage_dealt = attack(player_health, enemy_health)
            print("You dealt {} damage to the enemy.".format(damage_dealt))
            player_health, damage_received = attack(enemy_health, player_health)
            print("Enemy dealt {} damage to you.".format(damage_received))
        elif choice == '2':
            print("You ran away from the battle!")
            break
        
    if player_health <= 0:
        print("You have been defeated!")
    elif enemy_health <= 0:
        print("You have defeated the enemy!")
        
battle()

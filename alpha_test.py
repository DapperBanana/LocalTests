
import random

player_health = 100
player_attack = 10
player_defense = 5

enemy_health = 50
enemy_attack = 5
enemy_defense = 2

def attack(attacker_health, attacker_attack, defender_health, defender_defense):
    damage = max(attacker_attack - defender_defense, 0)
    defender_health -= damage
    return defender_health

def player_turn():
    print("Player's Turn:")
    action = input("Enter 'a' to attack: ")

    if action == 'a':
        global enemy_health
        enemy_health = attack(player_health, player_attack, enemy_health, enemy_defense)
        print(f"Player attacks! Enemy health: {enemy_health}")

def enemy_turn():
    print("Enemy's Turn:")
    global player_health
    player_health = attack(enemy_health, enemy_attack, player_health, player_defense)
    print(f"Enemy attacks! Player health: {player_health}")

def main():
    print("Welcome to the Text RPG Game!")
    
    while player_health > 0 and enemy_health > 0:
        player_turn()
        if enemy_health <= 0:
            print("Enemy defeated! You win!")
            break
        enemy_turn()
        if player_health <= 0:
            print("Player defeated! Game over!")
            break

if __name__ == "__main__":
    main()

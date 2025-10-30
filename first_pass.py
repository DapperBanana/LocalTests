
import random

player_health = 100
player_attack = 10

enemy_health = 50
enemy_attack = 5

def player_turn():
    global enemy_health
    damage = random.randint(player_attack - 5, player_attack + 5)
    enemy_health -= damage
    print(f"You hit the enemy for {damage} damage. Enemy health: {enemy_health}")

def enemy_turn():
    global player_health
    damage = random.randint(enemy_attack - 3, enemy_attack + 3)
    player_health -= damage
    print(f"Enemy hits you for {damage} damage. Your health: {player_health}")

def main():
    print("Welcome to the RPG battle system!")
    
    while player_health > 0 and enemy_health > 0:
        player_turn()
        if enemy_health <= 0:
            print("You defeated the enemy!")
            break
        enemy_turn()
        if player_health <= 0:
            print("Game Over. You were defeated!")
            break

if __name__ == '__main__':
    main()

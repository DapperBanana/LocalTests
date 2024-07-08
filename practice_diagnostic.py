
import random

# Player stats
player_health = 100
player_attack = 10

# Enemy stats
enemy_health = 50
enemy_attack = 5

def player_turn():
    global enemy_health
    damage = random.randint(1, player_attack)
    enemy_health -= damage
    print(f"Player attacks and deals {damage} damage to the enemy.")

def enemy_turn():
    global player_health
    damage = random.randint(1, enemy_attack)
    player_health -= damage
    print(f"Enemy attacks and deals {damage} damage to the player.")

def battle():
    global player_health, enemy_health
    while player_health > 0 and enemy_health > 0:
        player_turn()
        if enemy_health <= 0:
            print("Player wins the battle!")
            break
        enemy_turn()
        if player_health <= 0:
            print("Enemy wins the battle!")
            break
        print(f"Player health: {player_health}, Enemy health: {enemy_health}")

if __name__ == "__main__":
    print("Welcome to the text-based RPG battle system!")
    print("Player stats - Health: 100, Attack: 10")
    print("Enemy stats - Health: 50, Attack: 5")
    print("Let the battle begin!")
    battle()

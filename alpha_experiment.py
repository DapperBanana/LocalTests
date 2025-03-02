
import random

print("Welcome to the Text-based RPG game!")

player_name = input("Enter your name: ")

player_health = 100
player_attack = 10

enemy_health = 50
enemy_attack = 5

def player_turn():
    global enemy_health
    damage = random.randint(1, player_attack)
    enemy_health -= damage
    print(f"You hit the enemy for {damage} damage.")
    if enemy_health <= 0:
        print("You defeated the enemy!")
        return True
    return False

def enemy_turn():
    global player_health
    damage = random.randint(1, enemy_attack)
    player_health -= damage
    print(f"The enemy hit you for {damage} damage.")
    if player_health <= 0:
        print("You were defeated by the enemy!")
        return True
    return False

def battle():
    global player_health, enemy_health
    while player_health > 0 and enemy_health > 0:
        player_won = player_turn()
        if player_won:
            break
        enemy_won = enemy_turn()
        if enemy_won:
            break

if __name__ == "__main__":
    print(f"Welcome, {player_name}! Let the battle begin.")
    battle()

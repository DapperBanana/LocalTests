
import random

def battle():
    player_health = 100
    enemy_health = 100

    while player_health > 0 and enemy_health > 0:
        player_attack = random.randint(5, 25)
        enemy_attack = random.randint(5, 20)

        print(f"Player attacks the enemy and deals {player_attack} damage.")
        enemy_health -= player_attack

        print(f"Enemy attacks the player and deals {enemy_attack} damage.")
        player_health -= enemy_attack

        print(f"Player Health: {player_health} | Enemy Health: {enemy_health}")
        print()

    if player_health <= 0:
        print("You have been defeated. Game over.")
    else:
        print("You have defeated the enemy. Congratulations!")

def start_game():
    print("Welcome to the RPG game!")
    print("You have encountered an enemy. Prepare for battle!")
    battle()

start_game()

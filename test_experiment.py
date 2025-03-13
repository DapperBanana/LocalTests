
import random

# Initialize player's attributes
player_hp = 100
player_attack = 10

# Initialize enemy's attributes
enemy_hp = 50
enemy_attack = 5

print("Welcome to the text-based spaceship game!")

while player_hp > 0:
    print("\nPlayer's HP:", player_hp)
    print("Enemy's HP:", enemy_hp)

    # Player's turn
    player_choice = input("Enter 'a' to attack or 'r' to run: ")

    if player_choice == 'a':
        enemy_hp -= player_attack
        print("You attack the enemy! Enemy's HP decreased to", enemy_hp)

    elif player_choice == 'r':
        print("You run away from the enemy!")
        break

    else:
        print("Invalid input. Please try again.")
        continue

    # Check if enemy is defeated
    if enemy_hp <= 0:
        print("You defeated the enemy!")
        break

    # Enemy's turn
    player_hp -= enemy_attack
    print("Enemy attacks you! Your HP decreased to", player_hp)

# Game over
if player_hp <= 0:
    print("Game over. You are defeated.")

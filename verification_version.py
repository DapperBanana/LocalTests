
import random

def print_slow(str):
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(0.1)
    print()

def print_stats():
    print(f"Player HP: {player_hp}")
    print(f"Enemy HP: {enemy_hp}")

player_hp = 100
enemy_hp = 50

print_slow("Welcome to the Text-Based RPG Game!")

while player_hp > 0 and enemy_hp > 0:
    print_stats()
    action = input("Do you want to attack (a) or defend (d)? ")

    if action == "a":
        player_damage = random.randint(10, 20)
        enemy_damage = random.randint(5, 15)
        enemy_hp -= player_damage
        player_hp -= enemy_damage
        print_slow("You attack the enemy!")
        print_slow(f"The enemy takes {player_damage} damage")
        print_slow(f"You take {enemy_damage} damage")
    elif action == "d":
        player_damage = random.randint(5, 10)
        enemy_damage = random.randint(0, 5)
        player_hp -= enemy_damage
        print_slow("You defend against the enemy!")
        print_slow(f"The enemy takes {enemy_damage} damage")
        print_slow(f"You take {player_damage} damage")
    else:
        print_slow("Invalid action, please try again")

if player_hp > 0:
    print_slow("Congratulations, you have defeated the enemy!")
else:
    print_slow("Game over, you have been defeated.")

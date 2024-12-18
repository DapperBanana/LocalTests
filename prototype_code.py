
import random

def fight():
    player_health = 100
    enemy_health = 100

    while player_health > 0 and enemy_health > 0:
        player_attack = random.randint(1, 20)
        enemy_attack = random.randint(1, 20)

        print("Player health:", player_health)
        print("Enemy health:", enemy_health)
        print("1. Attack")
        print("2. Run")

        choice = input()

        if choice == '1':
            enemy_health -= player_attack
            player_health -= enemy_attack
            print("You attack the enemy for", player_attack, "damage")
            print("The enemy attacks you for", enemy_attack, "damage")
        elif choice == '2':
            print("You run away from the battle")
            break
        else:
            print("Invalid choice")

    if player_health <= 0:
        print("You have been defeated!")
    elif enemy_health <= 0:
        print("You have defeated the enemy!")

print("Welcome to the RPG game!")
print("Press any key to start the game")
input()

fight()

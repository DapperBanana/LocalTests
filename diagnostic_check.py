
import random

def print_status(player_health, enemy_health):
    print(f"Player Health: {player_health}")
    print(f"Enemy Health: {enemy_health}")

def main():
    player_health = 100
    enemy_health = 100

    print("Welcome to the Spaceship Game! Your spaceship is under attack by enemy aliens.")
    print_status(player_health, enemy_health)

    while player_health > 0 and enemy_health > 0:
        player_attack = random.randint(10, 20)
        enemy_attack = random.randint(5, 15)

        print("\nYour spaceship attacks the enemy!")
        enemy_health -= player_attack
        print(f"Enemy takes {player_attack} damage.")
        print_status(player_health, enemy_health)

        if enemy_health <= 0:
            print("\nCongratulations! You have destroyed the enemy spaceship.")
            break

        print("\nThe enemy spaceship attacks you!")
        player_health -= enemy_attack
        print(f"You take {enemy_attack} damage.")
        print_status(player_health, enemy_health)

        if player_health <= 0:
            print("\nGame over! Your spaceship has been destroyed by the enemy.")
            break

if __name__ == "__main__":
    main()

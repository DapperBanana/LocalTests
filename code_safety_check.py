
import random

def attack(enemy_health):
    attack_dmg = random.randint(10, 20)
    enemy_health -= attack_dmg
    return enemy_health, attack_dmg

def defend(ship_health, enemy_dmg):
    ship_health -= enemy_dmg
    return ship_health

def check_win(ship_health, enemy_health):
    if ship_health <= 0:
        print("Game over! You have lost the battle.")
        return False
    elif enemy_health <= 0:
        print("Congratulations! You have defeated the enemy.")
        return False
    else:
        return True

def main():
    ship_health = 100
    enemy_health = 50

    print("Welcome to the text-based spaceship game!")
    print("Your goal is to defeat the enemy spaceship before it defeats you.")

    while True:
        print("\nYour spaceship health:", ship_health)
        print("Enemy spaceship health:", enemy_health)

        action = input("\nDo you want to [1] attack or [2] defend? ")

        if action == '1':
            enemy_health, attack_dmg = attack(enemy_health)
            print("You attack the enemy spaceship for", attack_dmg, "damage.")

        elif action == '2':
            enemy_dmg = random.randint(10, 15)
            ship_health = defend(ship_health, enemy_dmg)
            print("You defend against the enemy's attack and take", enemy_dmg, "damage.")

        else:
            print("Invalid input. Please choose 1 or 2.")

        if not check_win(ship_health, enemy_health):
            break

    print("Thank you for playing!")

if __name__ == "__main__":
    main()

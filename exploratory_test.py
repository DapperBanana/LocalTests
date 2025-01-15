
import random

def battle(enemy):
    print(f"You encounter a {enemy}!")
    player_health = 100
    enemy_health = 50

    while player_health > 0 and enemy_health > 0:
        print(f"Player Health: {player_health}")
        print(f"{enemy} Health: {enemy_health}")

        player_action = input("Do you want to attack or run? ").lower()

        if player_action == "attack":
            player_damage = random.randint(5, 20)
            enemy_damage = random.randint(5, 15)
            enemy_health -= player_damage
            player_health -= enemy_damage
            print(f"You attack the {enemy} and deal {player_damage} damage!")
            print(f"The {enemy} attacks you and deals {enemy_damage} damage!")

        elif player_action == "run":
            print("You ran away from the battle!")
            return False
        
        else:
            print("Invalid action, please try again.")

    if player_health <= 0:
        print("You have been defeated!")
        return False
    else:
        print(f"You have defeated the {enemy}!")
        return True

def main():
    print("Welcome to the RPG game!")
    print("You are on a quest to defeat the evil monsters.\n")

    enemies = ["Goblin", "Orc", "Dragon", "Skeleton"]

    while True:
        enemy = random.choice(enemies)
        result = battle(enemy)

        if not result:
            play_again = input("Do you want to play again? (yes/no) ").lower()
            if play_again != "yes":
                break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()

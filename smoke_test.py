
import random

def fight_enemy(enemy):
    player_health = 100
    enemy_health = random.randint(50, 100)

    print(f"You've encountered a {enemy} with {enemy_health} health.\n")

    while player_health > 0 and enemy_health > 0:
        attack = random.randint(1, 20)
        enemy_attack = random.randint(1, 15)

        print(f"Your attack: {attack}")
        enemy_health -= attack

        if enemy_health <= 0:
            print(f"You defeated the {enemy}!")
            break

        print(f"{enemy} attacks: {enemy_attack}")
        player_health -= enemy_attack

        if player_health <= 0:
            print("Game over. You were defeated.")
            break

        print(f"Your health: {player_health}\n{enemy} health: {enemy_health}\n")

def main():
    print("Welcome to the RPG Game!\n")

    while True:
        choice = input("Do you want to fight an enemy? (yes/no): ")

        if choice.lower() == "yes":
            enemies = ["Goblin", "Orc", "Dragon"]
            enemy = random.choice(enemies)
            fight_enemy(enemy)
        else:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

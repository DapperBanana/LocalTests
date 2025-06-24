
import random

def main():
    player = {
        "name": input("Enter your name: "),
        "health": 100,
        "attack": 10,
        "gold": 0
    }
    while player["health"] > 0:
        print("\n=================")
        print(f"Name: {player['name']}\nHealth: {player['health']}\nGold: {player['gold']}")
        print("=================")
        print("1. Explore\n2. Visit shop\n3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            explore(player)
        elif choice == "2":
            visit_shop(player)
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, try again.")

def explore(player):
    print("Exploring...")
    enemy = {
        "name": "Goblin",
        "health": 30,
        "attack": 5,
        "gold": 10
    }
    print(f"Encountered a {enemy['name']}!")
    while player["health"] > 0 and enemy["health"] > 0:
        print("\nYour turn:")
        print("1. Attack\n2. Run")
        choice = input("Enter your choice: ")
        if choice == "1":
            player_attack = random.randint(1, player["attack"])
            enemy["health"] -= player_attack
            print(f"You attacked the {enemy['name']} for {player_attack} damage!")
            if enemy["health"] <= 0:
                print(f"Defeated the {enemy['name']}!")
                player["gold"] += enemy["gold"]
                break
            print(f"{enemy['name']}'s health: {enemy['health']}")
            enemy_attack = random.randint(1, enemy["attack"])
            player["health"] -= enemy_attack
            print(f"The {enemy['name']} attacked you for {enemy_attack} damage!")
            print(f"Your health: {player['health']}")
        elif choice == "2":
            print("Ran away!")
            break
    if player["health"] <= 0:
        print("Game over, you died.")
    input("Press Enter to continue...")

def visit_shop(player):
    print("Welcome to the shop!")
    print(f"Gold: {player['gold']}")
    print("1. Buy health potion (20 gold)")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        if player["gold"] >= 20:
            player["gold"] -= 20
            player["health"] += 20
            print("Bought health potion, +20 health.")
        else:
            print("Not enough gold.")
    elif choice == "2":
        print("Leaving shop.")
    input("Press Enter to continue...")

if __name__ == "__main__":
    main()

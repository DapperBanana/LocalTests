
import random

player = {
    "name": "Player",
    "health": 100,
    "attack": 10,
    "gold": 0
}

enemies = [
    {"name": "Goblin", "health": 50, "attack": 5, "gold": 10},
    {"name": "Orc", "health": 100, "attack": 15, "gold": 20},
    {"name": "Dragon", "health": 200, "attack": 20, "gold": 50}
]

def battle(enemy):
    print(f"You have encountered a {enemy['name']}!")
    while player["health"] > 0 and enemy["health"] > 0:
        player_damage = random.randint(1, player["attack"])
        enemy_damage = random.randint(1, enemy["attack"])

        print(f"{player['name']} attacks {enemy['name']} for {player_damage} damage!")
        enemy["health"] -= player_damage

        if enemy["health"] <= 0:
            print(f"{enemy['name']} has been defeated!")
            player["gold"] += enemy["gold"]
            break

        print(f"{enemy['name']} attacks {player['name']} for {enemy_damage} damage!")
        player["health"] -= enemy_damage

        if player["health"] <= 0:
            print("You have been defeated!")
            break

def shop():
    print("Welcome to the shop!")
    print(f"You have {player['gold']} gold.")
    print("Items for sale:")
    print("1. Health Potion (20 gold) - Restores 20 health")
    print("2. Attack Potion (30 gold) - Increases attack by 5")
    
    choice = input("Choose an item to buy (1/2) or enter any other key to exit: ")

    if choice == "1":
        if player["gold"] >= 20:
            player["gold"] -= 20
            player["health"] += 20
            print("You bought a Health Potion!")
        else:
            print("Not enough gold to buy Health Potion.")
    elif choice == "2":
        if player["gold"] >= 30:
            player["gold"] -= 30
            player["attack"] += 5
            print("You bought an Attack Potion!")
        else:
            print("Not enough gold to buy Attack Potion.")

def main():
    print("Welcome to the RPG game!")

    while True:
        print("\n1. Battle")
        print("2. Shop")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            enemy = random.choice(enemies)
            battle(enemy)
        elif choice == "2":
            shop()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

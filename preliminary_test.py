
import random

player = {
    "name": "Player",
    "health": 100,
    "attack": 10,
    "potions": 3
}

monsters = [{"name": "Goblin", "health": 20, "attack": 5},
            {"name": "Orc", "health": 30, "attack": 8},
            {"name": "Dragon", "health": 50, "attack": 15}]

def main():
    print("Welcome to the RPG game!")
    player_name = input("Enter your name: ")
    player["name"] = player_name

    while True:
        print("\n" + player["name"] + ", HP: " + str(player["health"]))
        print("1. Fight")
        print("2. Drink potion")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            monster = random.choice(monsters)
            print("A " + monster["name"] + " appears!")

            while player["health"] > 0 and monster["health"] > 0:
                player_dmg = random.randint(1, player["attack"])
                monster_dmg = random.randint(1, monster["attack"])

                print("You deal " + str(player_dmg) + " damage to the " + monster["name"])
                monster["health"] -= player_dmg

                if monster["health"] <= 0:
                    print("You defeated the " + monster["name"])
                    break

                print("The " + monster["name"] + " deals " + str(monster_dmg) + " damage to you")
                player["health"] -= monster_dmg

                if player["health"] <= 0:
                    print("You were defeated by the " + monster["name"])
                    break

        elif choice == "2":
            if player["potions"] > 0:
                player["potions"] -= 1
                player["health"] += 20
                print("You drink a potion and restore 20 HP")
            else:
                print("You have no potions left!")

        elif choice == "3":
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

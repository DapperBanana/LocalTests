
import random

player = {
    "name": "Player",
    "health": 100,
    "attack": 10,
    "gold": 0
}

def battle():
    enemy = {
        "name": "Monster",
        "health": random.randint(50, 100),
        "attack": random.randint(5, 15)
    }

    print(f"A wild {enemy['name']} appears!")

    while player['health'] > 0 and enemy['health'] > 0:
        print(f"{player['name']}\'s health: {player['health']}")
        print(f"{enemy['name']}\'s health: {enemy['health']}")

        player_attack = random.randint(1, player['attack'])
        enemy_attack = random.randint(1, enemy['attack'])

        print(f"{player['name']} attacks {enemy['name']} for {player_attack} damage!")
        enemy['health'] -= player_attack

        print(f"{enemy['name']} attacks {player['name']} for {enemy_attack} damage!")
        player['health'] -= enemy_attack

    if player['health'] <= 0:
        print("You have been defeated. Game over.")
    else:
        player['gold'] += random.randint(10, 20)
        print(f"You have defeated the {enemy['name']}! You gained {player['gold']} gold.")

while True:
    choice = input("Enter 'battle' to start a battle, 'stats' to check your stats, or 'quit' to end the game: ")

    if choice == 'battle':
        battle()
    elif choice == 'stats':
        print(f"Name: {player['name']}")
        print(f"Health: {player['health']}")
        print(f"Attack: {player['attack']}")
        print(f"Gold: {player['gold']}")
    elif choice == 'quit':
        break
    else:
        print("Invalid choice. Please try again.")

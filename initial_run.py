
import random

player = {
    "name": "Player",
    "health": 100,
    "attack": 20,
    "defense": 10
}

enemy = {
    "name": "Enemy",
    "health": 50,
    "attack": 10,
    "defense": 5
}

def battle(player, enemy):
    print(f"A wild {enemy['name']} appeared!\n")

    while player['health'] > 0 and enemy['health'] > 0:
        player_damage = max(0, player['attack'] - enemy['defense'])
        enemy_damage = max(0, enemy['attack'] - player['defense'])

        print(f"{player['name']} attacks {enemy['name']} for {player_damage} damage!")
        enemy['health'] -= player_damage

        if enemy['health'] <= 0:
            print(f"{enemy['name']} has been defeated!")
            break

        print(f"{enemy['name']} attacks {player['name']} for {enemy_damage} damage!")
        player['health'] -= enemy_damage

        if player['health'] <= 0:
            print(f"{player['name']} has been defeated!")
            break

        print(f"{player['name']} HP: {player['health']}  {enemy['name']} HP: {enemy['health']}\n")

battle(player, enemy)

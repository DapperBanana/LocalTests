
import random

player = {
    'name': 'Player',
    'health': 100,
    'attack': 10,
    'defense': 5
}

enemy = {
    'name': 'Enemy',
    'health': 50,
    'attack': 8,
    'defense': 3
}

def battle(player, enemy):
    while player['health'] > 0 and enemy['health'] > 0:
        player_damage = max(0, player['attack'] - enemy['defense'])
        enemy_damage = max(0, enemy['attack'] - player['defense'])

        print(f"{player['name']} attacks {enemy['name']} for {player_damage} damage!")
        enemy['health'] -= player_damage

        print(f"{enemy['name']} attacks {player['name']} for {enemy_damage} damage!")
        player['health'] -= enemy_damage

        print(f"{player['name']} Health: {player['health']}")
        print(f"{enemy['name']} Health: {enemy['health']}")
        print("----------------------------")

    if player['health'] <= 0:
        print(f"{player['name']} has been defeated. Game Over.")
    else:
        print(f"{enemy['name']} has been defeated. You win!")

battle(player, enemy)

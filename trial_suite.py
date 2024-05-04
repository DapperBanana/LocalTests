
import random

# Create player and enemy objects
player = {
    "name": "Player",
    "health": 100,
    "attack": 10,
    "defense": 5
}

enemy = {
    "name": "Enemy",
    "health": 50,
    "attack": 8,
    "defense": 3
}

def battle(player, enemy):
    print(f"{player['name']} vs {enemy['name']}! Let the battle begin!")

    while player['health'] > 0 and enemy['health'] > 0:
        player_damage = max(0, player['attack'] - enemy['defense'])
        enemy_damage = max(0, enemy['attack'] - player['defense'])

        enemy['health'] -= player_damage
        player['health'] -= enemy_damage

        print(f"{player['name']} attacks {enemy['name']} and deals {player_damage} damage!")
        print(f"{enemy['name']} attacks {player['name']} and deals {enemy_damage} damage!")
        print(f"{player['name']} has {player['health']} health left.")
        print(f"{enemy['name']} has {enemy['health']} health left.")

    if player['health'] <= 0:
        print(f"{player['name']} was defeated! Game over.")
    else:
        print(f"{enemy['name']} was defeated! Congratulations, you win!")

# Start the battle
battle(player, enemy)

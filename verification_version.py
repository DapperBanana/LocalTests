
import random

player = {
    'name': 'Hero',
    'health': 100,
    'attack': 20,
    'defense': 10
}

enemy = {
    'name': 'Monster',
    'health': 50,
    'attack': 15,
    'defense': 5
}

def battle(player, enemy):
    print(f"{player['name']} vs {enemy['name']}")

    while player['health'] > 0 and enemy['health'] > 0:
        player_damage = max(0, player['attack'] - enemy['defense'])
        enemy['health'] -= player_damage
        print(f"{player['name']} attacks {enemy['name']} for {player_damage} damage. {enemy['name']}'s health: {enemy['health']}")

        if enemy['health'] <= 0:
            print(f"{player['name']} wins!")
            break

        enemy_damage = max(0, enemy['attack'] - player['defense'])
        player['health'] -= enemy_damage
        print(f"{enemy['name']} attacks {player['name']} for {enemy_damage} damage. {player['name']}'s health: {player['health']}")

        if player['health'] <= 0:
            print(f"{enemy['name']} wins!")

# Start the battle
battle(player, enemy)

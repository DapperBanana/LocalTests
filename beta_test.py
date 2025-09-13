
import random

player = {
    'name': 'Player',
    'hp': 100,
    'attack': 10,
    'defense': 5
}

enemy = {
    'name': 'Enemy',
    'hp': 50,
    'attack': 8,
    'defense': 3
}

def attack(attacker, defender):
    damage = max(0, attacker['attack'] - defender['defense'])
    defender['hp'] -= damage
    print(f"{attacker['name']} attacks {defender['name']} for {damage} damage!")

def battle(player, enemy):
    while player['hp'] > 0 and enemy['hp'] > 0:
        print(f"{player['name']} HP: {player['hp']} | {enemy['name']} HP: {enemy['hp']}")
        attack(player, enemy)
        if enemy['hp'] <= 0:
            print(f"{enemy['name']} has been defeated! {player['name']} wins!")
            break
        attack(enemy, player)
        if player['hp'] <= 0:
            print(f"{player['name']} has been defeated! {enemy['name']} wins!")
            break

battle(player, enemy)

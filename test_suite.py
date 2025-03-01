
import random

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

def attack(attacker, defender):
    damage = max(0, attacker["attack"] - defender["defense"])
    defender["health"] -= damage
    return damage

def battle(player, enemy):
    while player["health"] > 0 and enemy["health"] > 0:
        player_damage = attack(player, enemy)
        enemy_damage = attack(enemy, player)
        
        print(f"{player['name']} attacks {enemy['name']} for {player_damage} damage!")
        print(f"{enemy['name']} attacks {player['name']} for {enemy_damage} damage!")
        
        print(f"{player['name']} Health: {player['health']} Enemy Health: {enemy['health']}")
        
    if player["health"] <= 0:
        print("You have been defeated!")
    else:
        print("You have defeated the enemy!")

battle(player, enemy)

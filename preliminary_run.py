
import random

player = {
    "name": "Player",
    "health": 100,
    "attack": 10,
    "defence": 5
}

enemy = {
    "name": "Enemy",
    "health": 50,
    "attack": 5,
    "defence": 2
}

def attack(attacker, defender):
    damage = max(attacker["attack"] - defender["defence"], 0)
    defender["health"] -= damage
    return damage

def battle(player, enemy):
    while player["health"] > 0 and enemy["health"] > 0:
        player_damage = attack(player, enemy)
        enemy_damage = attack(enemy, player)
        
        print(f"{player['name']} attacks {enemy['name']} for {player_damage} damage.")
        print(f"{enemy['name']} attacks {player['name']} for {enemy_damage} damage.")
        
        print(f"{player['name']} health: {player['health']}")
        print(f"{enemy['name']} health: {enemy['health']}")
        print("\n")
        
        if player["health"] <= 0:
            print("You have been defeated!")
        elif enemy["health"] <= 0:
            print("You have defeated the enemy!")
            
battle(player, enemy)

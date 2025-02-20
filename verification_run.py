
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

def calculate_damage(attacker, defender):
    damage = attacker["attack"] - defender["defense"]
    if damage < 0:
        damage = 0
    return damage

def battle(player, enemy):
    while player["health"] > 0 and enemy["health"] > 0:
        player_damage = calculate_damage(player, enemy)
        enemy_damage = calculate_damage(enemy, player)
        
        print(f"{player['name']} attacks {enemy['name']} for {player_damage} damage!")
        enemy["health"] -= player_damage
        print(f"{enemy['name']} attacks {player['name']} for {enemy_damage} damage!")
        player["health"] -= enemy_damage
        
        print(f"{player['name']} health: {player['health']}")
        print(f"{enemy['name']} health: {enemy['health']}")
        
        input("Press enter to continue the battle...")
    
    if player["health"] <= 0:
        print("Game Over! You have been defeated.")
    else:
        print("You have defeated the enemy! Victory!")

battle(player, enemy)

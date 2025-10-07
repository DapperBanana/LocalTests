
import random

# Player and enemy attributes
player = {
    "name": "Player",
    "hp": 100,
    "attack": 10,
    "defense": 5,
    "speed": 5
}

enemy = {
    "name": "Enemy",
    "hp": 50,
    "attack": 5,
    "defense": 2,
    "speed": 2
}

# Battle function
def battle(player, enemy):
    print(f"{player['name']} vs {enemy['name']}")
    while player["hp"] > 0 and enemy["hp"] > 0:
        # Player attacks enemy
        player_damage = max(0, player["attack"] - enemy["defense"])
        enemy["hp"] -= player_damage
        print(f"{player['name']} attacks {enemy['name']} for {player_damage} damage")
        
        # Check if enemy is defeated
        if enemy["hp"] <= 0:
            print(f"{enemy['name']} is defeated!")
            break
        
        # Enemy attacks player
        enemy_damage = max(0, enemy["attack"] - player["defense"])
        player["hp"] -= enemy_damage
        print(f"{enemy['name']} attacks {player['name']} for {enemy_damage} damage")
        
        # Check if player is defeated
        if player["hp"] <= 0:
            print(f"{player['name']} is defeated!")
            break
    
    print("Battle over")

# Start the battle
battle(player, enemy)


import random

player = {
    "name": "Hero",
    "health": 100,
    "attack": 20,
    "defense": 10
}

enemy = {
    "name": "Monster",
    "health": 50,
    "attack": 15,
    "defense": 5
}

def player_attack():
    damage = player["attack"] - enemy["defense"]
    enemy["health"] -= damage
    print(f"{player['name']} attacks {enemy['name']} for {damage} damage.")

def enemy_attack():
    damage = enemy["attack"] - player["defense"]
    player["health"] -= damage
    print(f"{enemy['name']} attacks {player['name']} for {damage} damage.")

def battle():
    while player["health"] > 0 and enemy["health"] > 0:
        player_attack()
        if enemy["health"] <= 0:
            print(f"{enemy['name']} has been defeated!")
            break
        enemy_attack()
        if player["health"] <= 0:
            print(f"{player['name']} has been defeated!")
            break
        
        print(f"{player['name']} health: {player['health']}")
        print(f"{enemy['name']} health: {enemy['health']}")

if __name__ == "__main__":
    print("Welcome to the battle!")
    battle()


import random

player = {
    "name": "Player",
    "health": 100,
    "attack": 10
}

enemy = {
    "name": "Enemy",
    "health": 50,
    "attack": 5
}

def player_attack():
    damage = player["attack"] + random.randint(-5, 5)
    enemy["health"] -= damage
    print(f"{player['name']} attacks {enemy['name']} for {damage} damage.")

def enemy_attack():
    damage = enemy["attack"] + random.randint(-3, 3)
    player["health"] -= damage
    print(f"{enemy['name']} attacks {player['name']} for {damage} damage.")

def battle():
    print("A wild enemy appeared!\n")
    
    while player["health"] > 0 and enemy["health"] > 0:
        print(f"{player['name']}: {player['health']} HP")
        print(f"{enemy['name']}: {enemy['health']} HP\n")
        
        player_attack()
        if enemy["health"] <= 0:
            print(f"{enemy['name']} was defeated! You win!")
            break
        
        enemy_attack()
        if player["health"] <= 0:
            print(f"{player['name']} was defeated! You lose!")
            break

battle()

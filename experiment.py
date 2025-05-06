
import random
import time

player = {
    "name": "Player",
    "health": 100,
    "attack": 20,
    "defense": 10
}

enemy = {
    "name": "Enemy",
    "health": 50,
    "attack": 10,
    "defense": 5
}

def player_attack():
    damage = random.randint(player["attack"] - 5, player["attack"] + 5)
    enemy["health"] -= damage
    print(f"You attacked {enemy['name']} and dealt {damage} damage!")

def enemy_attack():
    damage = random.randint(enemy["attack"] - 3, enemy["attack"] + 3)
    player["health"] -= max(0, damage - player["defense"])
    print(f"{enemy['name']} attacked you and dealt {damage} damage!")

def battle():
    print("A wild enemy appears!")
    while player["health"] > 0 and enemy["health"] > 0:
        print(f"Player HP: {player['health']}  Enemy HP: {enemy['health']}")
        time.sleep(1)
        player_attack()
        if enemy["health"] <= 0:
            print("You defeated the enemy!")
            break
        time.sleep(1)
        enemy_attack()
        if player["health"] <= 0:
            print("You were defeated by the enemy!")
            break

battle()

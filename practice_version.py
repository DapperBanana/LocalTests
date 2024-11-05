
import random

player = {
    "name": "Player",
    "health": 100,
    "attack": 10,
    "heal": 20
}

enemy = {
    "name": "Enemy",
    "health": 50,
    "attack": 5
}

def print_status():
    print(f"{player['name']} Health: {player['health']}")
    print(f"{enemy['name']} Health: {enemy['health']}")

def player_turn():
    action = input("Choose an action - (attack/heal): ")
    if action == "attack":
        damage = random.randint(1, player['attack'])
        enemy['health'] -= damage
        print(f"{player['name']} attacks {enemy['name']} for {damage} damage!")
    elif action == "heal":
        heal_amount = random.randint(1, player['heal'])
        player['health'] += heal_amount
        print(f"{player['name']} heals for {heal_amount} health points!")
    else:
        print("Invalid action, try again.")

def enemy_turn():
    damage = random.randint(1, enemy['attack'])
    player['health'] -= damage
    print(f"{enemy['name']} attacks {player['name']} for {damage} damage!")

print("Welcome to the RPG Battle System!")

while player['health'] > 0 and enemy['health'] > 0:
    print_status()
    
    player_turn()
    if enemy['health'] <= 0:
        print("You defeated the enemy!")
        break
    
    enemy_turn()
    if player['health'] <= 0:
        print("You were defeated by the enemy!")
        break

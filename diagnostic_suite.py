
import random

player = {"name": "Player", "health": 100, "attack": 10, "heal": 20}
enemy = {"name": "Enemy", "health": 50, "attack": 5}

def battle(player, enemy):
    print("A wild {} appears!".format(enemy["name"]))
    
    while player["health"] > 0 and enemy["health"] > 0:
        print("\n{}'s health: {}".format(player["name"], player["health"]))
        print("{}'s health: {}".format(enemy["name"], enemy["health"])

        action = input("\nEnter 'attack' to attack or 'heal' to heal: ")

        if action == "attack":
            enemy["health"] -= player["attack"]
            print("You attack the {} for {} damage!".format(enemy["name"], player["attack"]))
        elif action == "heal":
            player["health"] += player["heal"]
            print("You heal yourself for {} health!".format(player["heal"]))
        
        player_damage = random.randint(1, enemy["attack"])
        player["health"] -= player_damage
        print("The {} attacks you for {} damage!".format(enemy["name"], player_damage))

    if player["health"] <= 0:
        print("You have been defeated! Game over.")
    else:
        print("You have defeated the enemy! Congratulations!")

battle(player, enemy)

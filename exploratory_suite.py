
import random

player_health = 100
enemy_health = 100

def attack(player):
    return random.randint(10, 20)

def enemy_attack():
    return random.randint(5, 15)

print("Welcome to the Text-Based RPG game!")

while player_health > 0 and enemy_health > 0:
    player_damage = attack('Player')
    enemy_damage = enemy_attack()

    print("Player attacks and deals {} damage to the enemy.".format(player_damage))
    enemy_health -= player_damage

    if enemy_health <= 0:
        print("Player wins! Enemy defeated.")
        break

    print("Enemy attacks and deals {} damage to the player.".format(enemy_damage))
    player_health -= enemy_damage

    if player_health <= 0:
        print("Enemy wins! Player defeated.")
        break

    print("Player health: {}".format(player_health))
    print("Enemy health: {}".format(enemy_health))

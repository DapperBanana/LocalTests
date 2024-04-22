
import random

player_hp = 100
player_attack = 10
player_defense = 5

enemy_hp = 50
enemy_attack = 8
enemy_defense = 3

def player_turn():
    global enemy_hp
    enemy_hp -= max(0, player_attack - enemy_defense)
    print("Player attacks!")
    print("Enemy HP:", enemy_hp)

def enemy_turn():
    global player_hp
    player_hp -= max(0, enemy_attack - player_defense)
    print("Enemy attacks!")
    print("Player HP:", player_hp)

def battle():
    global player_hp, enemy_hp
    while player_hp > 0 and enemy_hp > 0:
        turn = random.randint(0, 1) # 0: player's turn, 1: enemy's turn
        if turn == 0:
            player_turn()
        else:
            enemy_turn()
    
    if player_hp <= 0:
        print("You were defeated!")
    else:
        print("You defeated the enemy!")

print("A wild enemy appears!")
battle()

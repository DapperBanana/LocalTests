
import random

player_hp = 100
enemy_hp = 100

def player_attack():
    return random.randint(5, 15)

def enemy_attack():
    return random.randint(5, 15)

def battle():
    global player_hp, enemy_hp
    
    while player_hp > 0 and enemy_hp > 0:
        player_dmg = player_attack()
        enemy_dmg = enemy_attack()
        
        print("Player attacks and deals", player_dmg, "damage")
        enemy_hp -= player_dmg
        
        if enemy_hp <= 0:
            print("Enemy defeated! Player wins!")
            break
        
        print("Enemy attacks and deals", enemy_dmg, "damage")
        player_hp -= enemy_dmg
        
        if player_hp <= 0:
            print("Player defeated! Enemy wins!")
            break
        
        print("Player HP:", player_hp)
        print("Enemy HP:", enemy_hp)
        print("\n")

battle()

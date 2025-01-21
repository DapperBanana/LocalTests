
import random

player_hp = 100
enemy_hp = 100

def player_attack():
    damage = random.randint(10, 20)
    return damage

def enemy_attack():
    damage = random.randint(5, 15)
    return damage

def battle():
    global player_hp
    global enemy_hp
    print("A wild enemy appears!")
    
    while player_hp > 0 and enemy_hp > 0:
        print("Player HP:", player_hp)
        print("Enemy HP:", enemy_hp)
        player_action = input("Choose an action: (1) Attack\n")
        
        if player_action == '1':
            player_damage = player_attack()
            print("Player attacks and deals", player_damage, "damage")
            enemy_hp -= player_damage
            
            if enemy_hp <= 0:
                print("Player wins!")
                break
            
            enemy_damage = enemy_attack()
            print("Enemy attacks and deals", enemy_damage, "damage")
            player_hp -= enemy_damage
            
            if player_hp <= 0:
                print("Enemy wins!")
                break
            
        else:
            print("Invalid action. Please choose again.")
            

battle()

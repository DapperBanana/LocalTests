
import random

# Player and enemy stats
player_hp = 100
player_attack = 10
enemy_hp = 50
enemy_attack = 5

def battle():
    global player_hp, enemy_hp
    
    print("A wild enemy appears!")
    
    while player_hp > 0 and enemy_hp > 0:
        player_damage = random.randint(1, player_attack)
        enemy_damage = random.randint(1, enemy_attack)
        
        print("Player attacks the enemy for", player_damage, "damage!")
        enemy_hp -= player_damage
        print("Enemy HP:", enemy_hp)
        
        if enemy_hp <= 0:
            print("Player defeated the enemy!")
            break
        
        print("Enemy attacks the player for", enemy_damage, "damage!")
        player_hp -= enemy_damage
        print("Player HP:", player_hp)
        
        if player_hp <= 0:
            print("Player was defeated!")
            break

if __name__ == "__main__":
    battle()

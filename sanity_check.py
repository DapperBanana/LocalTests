
import random

player_hp = 100
enemy_hp = 100

def player_attack():
    return random.randint(10, 20)

def enemy_attack():
    return random.randint(5, 15)

def battle():
    global player_hp
    global enemy_hp

    while player_hp > 0 and enemy_hp > 0:
        print("Player HP:", player_hp)
        print("Enemy HP:", enemy_hp)
        input("Press Enter to attack!")
        
        player_dmg = player_attack()
        enemy_dmg = enemy_attack()
        
        enemy_hp -= player_dmg
        print("Player hits the enemy for", player_dmg, "damage!")
        
        if enemy_hp <= 0:
            print("Player wins!")
            break
        
        player_hp -= enemy_dmg
        print("Enemy hits the player for", enemy_dmg, "damage!")
        
        if player_hp <= 0:
            print("Enemy wins!")
            break

if __name__ == "__main__":
    print("Welcome to the RPG battle!")
    battle()


import random

player_hp = 100
player_attack = 20
enemy_hp = 50
enemy_attack = 10

print("Welcome to the Text-Based RPG Battle!")

while player_hp > 0 and enemy_hp > 0:
    player_damage = random.randint(0, player_attack)
    enemy_damage = random.randint(0, enemy_attack)
    
    print("\nPlayer HP:", player_hp)
    print("Enemy HP:", enemy_hp)
    print("\n1. Attack")
    print("2. Defend")
    choice = input("Choose your action: ")
    
    if choice == "1":
        enemy_hp -= player_damage
        print("You dealt", player_damage, "damage to the enemy!")
    elif choice == "2":
        player_hp -= (enemy_damage // 2)
        print("You defended against the enemy's attack!")
        
    player_hp -= enemy_damage
    print("The enemy dealt", enemy_damage, "damage to you!")
    
if player_hp <= 0:
    print("You have been defeated. Game over.")
elif enemy_hp <= 0:
    print("You have defeated the enemy! Congratulations!")

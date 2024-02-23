
import random

def attack(player_name, enemy_name):
    player_hp = 100
    enemy_hp = 100

    while player_hp > 0 and enemy_hp > 0:
        player_damage = random.randint(5, 15)
        enemy_damage = random.randint(5, 15)

        print(f"{player_name} attacks {enemy_name} for {player_damage} damage!")
        enemy_hp -= player_damage
        print(f"{enemy_name} has {enemy_hp} HP left.")

        if enemy_hp <= 0:
            print(f"{player_name} has defeated {enemy_name}.")
            break

        print(f"{enemy_name} attacks {player_name} for {enemy_damage} damage!")
        player_hp -= enemy_damage
        print(f"{player_name} has {player_hp} HP left.")
        
        if player_hp <= 0:
            print(f"{enemy_name} has defeated {player_name}. Game over.")
            break

if __name__ == "__main__":
    player_name = input("Enter your character's name: ")
    enemy_name = input("Enter the enemy's name: ")

    print(f"A wild {enemy_name} appears! Battle begins!")
    
    attack(player_name, enemy_name)

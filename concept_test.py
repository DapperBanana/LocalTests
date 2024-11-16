
import random

player_health = 100
enemy_health = 100

def player_attack():
    damage = random.randint(10, 20)
    return damage

def enemy_attack():
    damage = random.randint(5, 15)
    return damage

def game_over():
    print("Game over. You have been defeated.")
    quit()

while player_health > 0 and enemy_health > 0:
    print("Player Health:", player_health)
    print("Enemy Health:", enemy_health)

    player_move = input("Enter 'a' to attack: ")

    if player_move == 'a':
        player_damage = player_attack()
        enemy_health -= player_damage
        print("You attacked the enemy for", player_damage, "damage")

        if enemy_health <= 0:
            print("You have defeated the enemy!")
            break

        enemy_damage = enemy_attack()
        player_health -= enemy_damage
        print("The enemy attacked you for", enemy_damage, "damage")

        if player_health <= 0:
            game_over()

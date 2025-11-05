
import random

player_health = 100
enemy_health = 100

def player_attack():
    damage = random.randint(10, 20)
    return damage

def enemy_attack():
    damage = random.randint(5, 15)
    return damage

def battle():
    global player_health, enemy_health

    while player_health > 0 and enemy_health > 0:
        print("Player health: ", player_health)
        print("Enemy health: ", enemy_health)
        input("Press Enter to attack")

        player_damage = player_attack()
        enemy_damage = enemy_attack()

        print("Player attacks and deals ", player_damage, " damage to enemy")
        enemy_health -= player_damage

        if enemy_health <= 0:
            print("Enemy has been defeated. Player wins!")
            break

        print("Enemy attacks and deals ", enemy_damage, " damage to player")
        player_health -= enemy_damage

        if player_health <= 0:
            print("Player has been defeated. Enemy wins!")
            break

if __name__ == "__main__":
    battle()

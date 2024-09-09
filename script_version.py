
import random

player_health = 100
enemy_health = random.randint(50, 100)

print("Welcome to Text RPG Game!")
print("Your current health: {}".format(player_health))
print("An enemy approaches with {} health.".format(enemy_health))

while player_health > 0 and enemy_health > 0:
    action = input("Would you like to attack or heal? (a/h): ")

    if action == 'a':
        player_attack = random.randint(10, 20)
        enemy_attack = random.randint(5, 15)

        enemy_health -= player_attack
        player_health -= enemy_attack

        print("You attack the enemy for {} damage.".format(player_attack))
        print("The enemy attacks you for {} damage.".format(enemy_attack))

    elif action == 'h':
        heal_amount = random.randint(10, 20)
        player_health += heal_amount

        print("You heal yourself for {} health.".format(heal_amount))

    else:
        print("Invalid input. Please try again.")

    print("Your current health: {}".format(player_health))
    print("Enemy's current health: {}".format(enemy_health))

if player_health > 0:
    print("Congratulations, you have defeated the enemy!")
else:
    print("Game over, you have been defeated.")

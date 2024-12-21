
import random

player_health = 100
player_attack = 10

enemy_health = random.randint(50, 100)
enemy_attack = random.randint(5, 15)

def battle():
    global player_health, enemy_health
    
    while player_health > 0 and enemy_health > 0:
        print("Player Health:", player_health)
        print("Enemy Health:", enemy_health)
        print("\n1. Attack\n2. Run")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            enemy_health -= player_attack
            player_health -= enemy_attack
            print("You attack the enemy for", player_attack, "damage")
            print("The enemy attacks you for", enemy_attack, "damage")
        elif choice == '2':
            print("You run away from the battle.")
            break
        else:
            print("Invalid choice. Try again.")
    
    if player_health <= 0:
        print("You have been defeated. Game over.")
    elif enemy_health <= 0:
        print("You have defeated the enemy. Congratulations!")

print("Welcome to the Text-based RPG Game!")
print("Your objective is to defeat the enemy.")

battle()

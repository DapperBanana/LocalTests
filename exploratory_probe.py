
import random

player_hp = 100
enemy_hp = 100

def player_attack():
    global enemy_hp
    damage = random.randint(10, 20)
    enemy_hp -= damage
    print(f"You attack the enemy and deal {damage} damage.")

def enemy_attack():
    global player_hp
    damage = random.randint(5, 15)
    player_hp -= damage
    print(f"The enemy attacks you and deals {damage} damage.")

def check_winner():
    if player_hp <= 0:
        print("You have been defeated. Game over.")
        return True
    elif enemy_hp <= 0:
        print("You have defeated the enemy. Congratulations!")
        return True
    return False

print("Welcome to the RPG battle system!")

while True:
    choice = input("Do you want to attack? (y/n): ")
    
    if choice.lower() == 'y':
        player_attack()
        enemy_attack()
        if check_winner():
            break
    elif choice.lower() == 'n':
        print("You decide to retreat. Game over.")
        break
    else:
        print("Invalid choice. Please choose again.")

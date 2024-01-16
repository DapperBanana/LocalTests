
import random

player_health = 100
enemy_health = 100

def attack():
    damage = random.randint(1, 20)
    return damage

def game_over():
    print("\nGame Over")
    exit()

print("=== RPG Game ===")
print("A vicious enemy is approaching. Defend yourself!\n")

while True:
    print("Player Health:", player_health)
    print("Enemy Health:", enemy_health)
    print("\n1. Attack")
    print("2. Quit")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        player_damage = attack()
        enemy_damage = attack()
        
        player_health -= enemy_damage
        enemy_health -= player_damage
        
        print("\nYou attacked the enemy and dealt", player_damage, "damage.")
        print("The enemy attacked you and dealt", enemy_damage, "damage.")
        
        if player_health <= 0 or enemy_health <= 0:
            if player_health <= 0:
                print("\nYou are defeated!")
            else:
                print("\nYou defeated the enemy!")
            game_over()
    
    elif choice == "2":
        game_over()
    
    else:
        print("\nInvalid choice! Please try again.")

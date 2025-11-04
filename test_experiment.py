
import random

player = {
    'name': '',
    'health': 100,
    'attack': 10,
    'gold': 0,
}

def start_game():
    print("Welcome to the Text-Based RPG Game!")
    player['name'] = input("Enter your name: ")
    print(f"Welcome, {player['name']}, let's start our adventure!")
    explore()

def explore():
    print("\nYou are in a dark forest. What would you like to do?")
    print("1. Go deeper into the forest")
    print("2. Rest and heal")
    print("3. Check inventory")
    print("4. Quit game")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        encounter_enemy()
    elif choice == '2':
        player['health'] = 100
        print("You have been fully healed.")
        explore()
    elif choice == '3':
        print_inventory()
    elif choice == '4':
        print("Thanks for playing! See you next time.")
    else:
        print("Invalid choice. Please try again.")
        explore()

def print_inventory():
    print("\nInventory:")
    print("Health: ", player['health'])
    print("Gold: ", player['gold'])
    input("\nPress any key to continue...")
    explore()

def encounter_enemy():
    enemy_health = random.randint(50, 100)
    
    print("\nYou have encountered an enemy!")
    
    while enemy_health > 0 and player['health'] > 0:
        print("\nEnemy Health: ", enemy_health)
        print("Player Health: ", player['health'])
        print("\nWhat would you like to do?")
        print("1. Attack")
        print("2. Flee")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            attack_damage = random.randint(5, 15)
            enemy_health -= attack_damage
            print(f"You have dealt {attack_damage} damage to the enemy.")
            
            player_damage = random.randint(5, 15)
            player['health'] -= player_damage
            print(f"The enemy has dealt {player_damage} damage to you.")
            
        elif choice == '2':
            print("You fled from the enemy.")
            explore()
        else:
            print("Invalid choice. Please try again.")
    
    if enemy_health <= 0:
        print("You have defeated the enemy!")
        player['gold'] += 50
        input("\nPress any key to continue...")
        explore()
    else:
        print("You have been defeated by the enemy. Game over.")
        print(f"Final stats: Health - {player['health']}, Gold - {player['gold']}")
        
start_game()

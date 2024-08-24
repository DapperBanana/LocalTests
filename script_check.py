
import random

# Initialize player stats
player_hp = 100
player_score = 0

# Define alien encounters
aliens = ['Xenomorph', 'Predator', 'Sauron', 'Thanos']

def encounter_alien():
    alien = random.choice(aliens)
    alien_hp = random.randint(50, 100)
    
    print(f"You encountered a {alien}! Battle begins...")
    
    while alien_hp > 0:
        player_attack = random.randint(10, 20)
        alien_attack = random.randint(5, 15)
        
        print(f"Your HP: {player_hp} | {alien}'s HP: {alien_hp}")
        
        player_hp -= alien_attack
        alien_hp -= player_attack
    
    if player_hp <= 0:
        print("Game over. You were defeated by the alien.")
    else:
        print(f"You defeated the {alien}!")
        player_score += 10

# Main game loop
while player_hp > 0:
    print("\n1. Encounter Alien")
    print("2. Exit Game")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        encounter_alien()
    elif choice == '2':
        print("Thanks for playing! Final score:", player_score)
        break
    else:
        print("Invalid choice. Please try again.")



import random

# Player's stats
player = {'HP': 100, 'attack': 10, 'defense': 5, 'gold': 0}

# Monster stats
monster = {'HP': 50, 'attack': 8, 'defense': 2, 'gold': 10}

def attack(attacker, defender):
    damage = max(0, attacker['attack'] - defender['defense'])
    defender['HP'] -= damage
    if defender['HP'] <= 0:
        defender['HP'] = 0

def print_stats():
    print("\nPlayer HP: {}".format(player['HP']))
    print("Monster HP: {}".format(monster['HP']))
    print("Gold: {}".format(player['gold']))

def main():
    print("Welcome to the text-based RPG game!")
    
    while player['HP'] > 0 and monster['HP'] > 0:
        print_stats()
        
        choice = input("\nDo you want to attack (a) or run (r)? ").lower()
        
        if choice == 'a':
            attack(player, monster)
            print("You attack the monster!")
            
            if monster['HP'] > 0:
                attack(monster, player)
                print("The monster attacks you!")

        elif choice == 'r':
            print("You run away!")
            break
        
        else:
            print("Invalid choice. Try again.")
    
    if player['HP'] <= 0:
        print("\nGame over! You have been defeated by the monster.")
    elif monster['HP'] <= 0:
        print("\nCongratulations! You have defeated the monster and collected {} gold.".format(monster['gold']))
        player['gold'] += monster['gold']

if __name__ == "__main__":
    main()

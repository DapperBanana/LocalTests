
import random

def print_divider():
    print("\n--------------------------------------------------\n")

def print_intro():
    print("Welcome to Text-Based RPG Game!")
    print_divider()
    print("You find yourself in a dark forest...")
    print("Your goal is to find the treasure hidden deep within!")
    print_divider()

def game_over():
    print("Game Over. Try again!")

def explore_forest():
    print("You start exploring the forest...")
    actions = ["fight", "run"]
    action = random.choice(actions)
    
    if action == "fight":
        print("You encountered a monster!")
        print("You must fight to survive!")
        combat()
    elif action == "run":
        print("You run away from danger...")
        print("You continue to explore the forest!")
        explore_forest()

def combat():
    player_health = 100
    monster_health = 50
    
    while player_health > 0 and monster_health > 0:
        player_attack = random.randint(1, 20)
        monster_attack = random.randint(1, 10)
        
        print("Player attacks with a power of", player_attack)
        monster_health -= player_attack
        print("Monster's health:", monster_health)
        
        print("Monster attacks with a power of", monster_attack)
        player_health -= monster_attack
        print("Player's health:", player_health)
        
    if player_health > 0:
        print("You defeated the monster!")
        print("You continue to explore the forest!")
        explore_forest()
    else:
        print("You were defeated by the monster!")
        game_over()

def main():
    print_intro()
    explore_forest()

if __name__ == "__main__":
    main()

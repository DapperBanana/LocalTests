
import random

player = {"name": "Player", "health": 100, "attack": 10, "gold": 0}
monsters = [{"name": "Goblin", "health": 20, "attack": 5, "gold": 10},
            {"name": "Orc", "health": 30, "attack": 8, "gold": 20},
            {"name": "Dragon", "health": 50, "attack": 15, "gold": 50}]

def show_status():
    print(f"{player['name']} - Health: {player['health']} - Gold: {player['gold']}")

def battle(monster):
    print(f"You encounter a {monster['name']}!")
    
    while player['health'] > 0 and monster['health'] > 0:
        player_damage = random.randint(1, player['attack'])
        monster_damage = random.randint(1, monster['attack'])
        
        print(f"{player['name']} attacks and deals {player_damage} damage")
        monster['health'] -= player_damage
        
        print(f"{monster['name']} attacks and deals {monster_damage} damage")
        player['health'] -= monster_damage
        
        show_status()
    
    if player['health'] <= 0:
        print("Game over! You have been defeated.")
    else:
        print(f"You defeated the {monster['name']} and earned {monster['gold']} gold!")
        player['gold'] += monster['gold']

def main():
    print("Welcome to the RPG game!")
    
    while player['health'] > 0:
        choice = input("Do you want to explore (1) or quit (2)? ")
        
        if choice == "1":
            monster = random.choice(monsters)
            battle(monster)
        elif choice == "2":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

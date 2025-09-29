
import random

player = {'name': 'Player', 'health': 100, 'attack': 10, 'gold': 0}
monsters = [{'name': 'Goblin', 'health': 20, 'attack': 5, 'gold': 10},
            {'name': 'Orc', 'health': 30, 'attack': 7, 'gold': 15},
            {'name': 'Dragon', 'health': 50, 'attack': 15, 'gold': 20}]

def print_status():
    print('Player\nHealth: {}\nGold: {}\n'.format(player['health'], player['gold']))

def battle(monster):
    print('You encounter a {}!'.format(monster['name']))
    while player['health'] > 0 and monster['health'] > 0:
        player_attack = random.randint(1, player['attack'])
        monster_attack = random.randint(1, monster['attack'])
        
        print('You attack the {} for {} damage.'.format(monster['name'], player_attack))
        monster['health'] -= player_attack
        
        if monster['health'] <= 0:
            print('You defeated the {}!'.format(monster['name']))
            player['gold'] += monster['gold']
            break
        
        print('{} attacks you for {} damage.'.format(monster['name'], monster_attack))
        player['health'] -= monster_attack
        
        print_status()
        
    if player['health'] <= 0:
        print('Game Over! You were defeated by the {}.'.format(monster['name']))

def explore():
    print('You explore the area...')
    
    monster = random.choice(monsters)
    battle(monster)

def main():
    print('Welcome to the RPG game!')
    
    while True:
        print_status()
        choice = input('Do you want to explore? (y/n) ').lower()
        
        if choice == 'y':
            explore()
        elif choice == 'n':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()

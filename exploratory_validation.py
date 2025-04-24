
import random

def main():
    print("Welcome to the Text-Based RPG Game!")
    player = create_character()
    enemy = create_enemy()
    
    while player['health'] > 0:
        print("\n------------------")
        print("Player stats:")
        print_stats(player)
        print("\nEnemy stats:")
        print_stats(enemy)
        
        action = get_player_action()
        
        if action == '1':
            attack(player, enemy)
            if enemy['health'] <= 0:
                print("You defeated the enemy!")
                enemy = create_enemy()
        elif action == '2':
            player['health'] += 10
            print("Player healed for 10 HP.")
        
        enemy_attack(player, enemy)
        
    print("\nGame over. You have died.")

def create_character():
    character = {
        'name': 'Player',
        'health': 100,
        'attack': 10,
        'defense': 5
    }
    return character

def create_enemy():
    enemies = ['Goblin', 'Skeleton', 'Orc', 'Dragon']
    enemy = {
        'name': random.choice(enemies),
        'health': random.randint(50, 100),
        'attack': random.randint(5, 15),
        'defense': random.randint(1, 10)
    }
    return enemy

def print_stats(entity):
    for key, value in entity.items():
        print(key + ':', value)

def get_player_action():
    print("\n1. Attack")
    print("2. Heal")
    action = input("Choose an action: ")
    return action

def attack(attacker, defender):
    damage = max(0, attacker['attack'] - defender['defense'])
    defender['health'] -= damage
    print(f"{attacker['name']} attacks {defender['name']} for {damage} damage.")

def enemy_attack(player, enemy):
    damage = max(0, enemy['attack'] - player['defense'])
    player['health'] -= damage
    print(f"{enemy['name']} attacks {player['name']} for {damage} damage.")

if __name__ == "__main__":
    main()

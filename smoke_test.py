
import random

def game():
    print("Welcome to the text-based RPG game!")
    
    player_health = 100
    player_attack = 20
    player_defense = 10
    player_gold = 0
    
    enemy_health = 50
    enemy_attack = 15
    enemy_defense = 5
    
    while player_health > 0:
        print("\nPlayer Stats:")
        print("Health: {}".format(player_health))
        print("Attack: {}".format(player_attack))
        print("Defense: {}".format(player_defense))
        print("Gold: {}".format(player_gold))
        
        print("\nEnemy Stats:")
        print("Health: {}".format(enemy_health))
        print("Attack: {}".format(enemy_attack))
        print("Defense: {}".format(enemy_defense))
        
        action = input("\nDo you want to attack (a) or run away (r)? ")
        
        if action == 'a':
            player_damage = max(0, player_attack - enemy_defense)
            enemy_damage = max(0, enemy_attack - player_defense)
            
            enemy_health -= player_damage
            player_health -= enemy_damage
            
            print("\nYou attack the enemy for {} damage.".format(player_damage))
            print("The enemy attacks you for {} damage.".format(enemy_damage))
            
            if enemy_health <= 0:
                print("\nYou defeated the enemy! You gain 10 gold.")
                player_gold += 10
                enemy_health = 50
                enemy_attack = random.randint(10, 20)
                enemy_defense = random.randint(0, 10)
        elif action == 'r':
            print("\nYou ran away from the battle.")
            break
        else:
            print("\nInvalid input. Please try again.")
    
    if player_health <= 0:
        print("\nGame over. You have been defeated.")
        print("Final gold: {}".format(player_gold))
    
    print("\nThank you for playing the text-based RPG game!")

game()

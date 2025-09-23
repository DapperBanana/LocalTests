
import random

player_health = 100
enemy_health = 100

def player_attack():
    return random.randint(10, 20)

def enemy_attack():
    return random.randint(5, 15)

def battle():
    global player_health
    global enemy_health
    
    print("A wild enemy appears! Time to battle!")
    
    while player_health > 0 and enemy_health > 0:
        print("Player Health:", player_health)
        print("Enemy Health:", enemy_health)
        print("1. Attack")
        print("2. Run")
        
        choice = input("Choose your action: ")
        
        if choice == '1':
            player_damage = player_attack()
            enemy_damage = enemy_attack()
            print("Player attacks and deals", player_damage, "damage!")
            enemy_health -= player_damage
            
            if enemy_health <= 0:
                print("Enemy defeated! You win!")
                break
            
            print("Enemy attacks and deals", enemy_damage, "damage!")
            player_health -= enemy_damage
            
            if player_health <= 0:
                print("Player defeated! Game over.")
                break
        
        elif choice == '2':
            print("You run away from the battle. Coward!")
            break
        
        else:
            print("Invalid choice. Please try again.")
        
        print("-------------------")
    
battle()

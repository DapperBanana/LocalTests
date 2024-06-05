
import random

def print_hp_bar(hp):
    print("HP [", end="")
    for i in range(hp):
        print("#", end="")
    for i in range(10-hp):
        print(" ", end="")
    print("]")

def main():
    print("Welcome to the Spaceship Game!")
    hp = 10
    enemy_hp = random.randint(1, 10)
    
    print("Your spaceship's HP:")
    print_hp_bar(hp)
    
    print("Enemy spaceship appears!")
    print("Enemy spaceship's HP:")
    print_hp_bar(enemy_hp)
    
    while hp > 0 and enemy_hp > 0:
        command = input("Enter a command (attack/heal): ").lower()
        
        if command == "attack":
            damage = random.randint(1, 4)
            enemy_hp -= damage
            print("You attack the enemy for", damage, "damage!")
        elif command == "heal":
            heal_amount = random.randint(1, 3)
            hp += heal_amount
            print("You heal yourself for", heal_amount, "HP!")
        else:
            print("Invalid command, try again.")
            continue
        
        print("Your spaceship's HP:")
        print_hp_bar(hp)
        
        print("Enemy spaceship's HP:")
        print_hp_bar(enemy_hp)
    
    if hp <= 0:
        print("Your spaceship has been destroyed. Game over!")
    else:
        print("You have destroyed the enemy spaceship. Congratulations, you win!")

if __name__ == "__main__":
    main()

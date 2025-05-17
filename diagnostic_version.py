
import random

def main():
    print("Welcome to the Space Adventure Game!")
    player_name = input("What is your name, Captain? ")

    player_health = 100
    alien_health = 100

    while player_health > 0 and alien_health > 0:
        print("\nPlayer Health:", player_health)
        print("Alien Health:", alien_health)

        command = input("\nEnter a command - 'attack' or 'heal': ").lower()

        if command == 'attack':
            player_damage = random.randint(10, 20)
            alien_damage = random.randint(5, 15)

            alien_health -= player_damage
            player_health -= alien_damage

            print("\nYou dealt", player_damage, "damage to the alien!")
            print("The alien dealt", alien_damage, "damage to you!")

        elif command == 'heal':
            player_heal = random.randint(10, 20)
            player_health += player_heal

            alien_damage = random.randint(5, 15)
            player_health -= alien_damage

            print("\nYou healed for", player_heal, "health!")
            print("The alien dealt", alien_damage, "damage to you!")

        else:
            print("\nInvalid command. Please enter 'attack' or 'heal'.")

    if player_health <= 0:
        print("\nGame Over. The alien has defeated you.")
    elif alien_health <= 0:
        print("\nCongratulations, Captain", player_name + "! You have defeated the alien and saved the galaxy!")

if __name__ == "__main__":
    main()

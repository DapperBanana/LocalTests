
import random

def print_line():
    print("=" * 50)

def fight_enemy(player_hp, player_attack, enemy_hp, enemy_attack):
    while player_hp > 0 and enemy_hp > 0:
        print_line()
        print("Player HP:", player_hp)
        print("Enemy HP:", enemy_hp)
        print_line()

        player_damage = random.randint(1, player_attack)
        enemy_damage = random.randint(1, enemy_attack)

        print("Player attacks and deals", player_damage, "damage.")
        enemy_hp -= player_damage

        if enemy_hp <= 0:
            print("Enemy defeated!")
            return True

        print("Enemy attacks and deals", enemy_damage, "damage.")
        player_hp -= enemy_damage

        if player_hp <= 0:
            print("Player defeated!")
            return False

def main():
    player_hp = 100
    player_attack = 20
    enemy_hp = random.randint(50, 100)
    enemy_attack = random.randint(10, 20)

    print_line()
    print("Welcome to the text-based RPG game!")
    print_line()

    while True:
        print_line()
        print("Player HP:", player_hp)
        print("Enemy HP:", enemy_hp)
        print_line()

        choice = input("Do you want to [A]ttack or [R]un away? ").upper()

        if choice == 'A':
            if fight_enemy(player_hp, player_attack, enemy_hp, enemy_attack):
                player_attack += 5
                player_hp += 10
                enemy_hp = random.randint(50, 100)
                enemy_attack = random.randint(10, 20)
            else:
                print("Game over. Thanks for playing!")
                break
        elif choice == 'R':
            print("You ran away from the battle. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

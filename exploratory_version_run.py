
import random

def print_board(player_position, enemy_position):
    for i in range(5):
        for j in range(5):
            if (i, j) == player_position:
                print("P", end=" ")
            elif (i, j) == enemy_position:
                print("E", end=" ")
            else:
                print("-", end=" ")
        print()

def fight():
    player_health = 100
    enemy_health = 50

    while player_health > 0 and enemy_health > 0:
        player_attack = random.randint(5, 20)
        enemy_attack = random.randint(5, 15)

        enemy_health -= player_attack
        player_health -= enemy_attack

        print(f"You hit the enemy for {player_attack} damage. Enemy health: {enemy_health}")
        print(f"Enemy hits you for {enemy_attack} damage. Your health: {player_health}")

    if player_health > 0:
        print("You defeated the enemy!")
    else:
        print("Game Over! You were defeated.")

def main():
    player_position = (0, 0)
    enemy_position = (4, 4)

    print("Welcome to the RPG game!")
    
    while True:
        print_board(player_position, enemy_position)

        direction = input("Enter direction (up, down, left, right) or q to quit: ")

        if direction == "q":
            break
        elif direction == "up":
            player_position = (max(player_position[0] - 1, 0), player_position[1])
        elif direction == "down":
            player_position = (min(player_position[0] + 1, 4), player_position[1])
        elif direction == "left":
            player_position = (player_position[0], max(player_position[1] - 1, 0))
        elif direction == "right":
            player_position = (player_position[0], min(player_position[1] + 1, 4))
        
        if player_position == enemy_position:
            print("You encountered an enemy!")
            fight()
            enemy_position = (random.randint(0, 4), random.randint(0, 4))

    print("Thanks for playing!")

if __name__ == "__main__":
    main()

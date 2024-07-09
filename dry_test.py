
import random

def print_status(health, fuel, distance):
    print(f"Health: {health} Fuel: {fuel} Distance: {distance}")
    print()

def spaceship_game():
    health = 100
    fuel = 50
    distance = 0

    while health > 0:
        print_status(health, fuel, distance)

        action = input("Choose an action - (a)ttack, (r)efuel, (m)ove, (q)uit: ")

        if action == 'a':
            damage = random.randint(1, 20)
            health -= damage
            print(f"You took {damage} damage!")

        elif action == 'r':
            refill = random.randint(10, 20)
            fuel += refill
            print(f"You refilled {refill} fuel!")

        elif action == 'm':
            if fuel >= 10:
                distance += 10
                fuel -= 10
                print("You moved 10 units!")

            else:
                print("Not enough fuel to move!")

        elif action == 'q':
            print("Thanks for playing!")
            break

        else:
            print("Invalid action! Please try again.")

    print_status(health, fuel, distance)
    print("Game over!")

if __name__ == "__main__":
    spaceship_game()

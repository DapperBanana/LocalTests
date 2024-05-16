
import random

def main():
    print("Welcome to the Spaceship Game!")

    health = 100
    fuel = 100
    distance = 0

    while health > 0 and fuel > 0:
        print("\nCurrent Stats:")
        print("Health: {}%".format(health))
        print("Fuel: {}%".format(fuel))
        print("Distance: {} light years".format(distance))

        action = input("\nChoose an action - [1] Travel, [2] Refuel, [3] Quit: ")

        if action == '1':
            travel_distance = random.randint(1, 10)
            travel_fuel = random.randint(1, 10)

            print("Traveling {} light years...".format(travel_distance))

            if travel_fuel > fuel:
                print("Not enough fuel to travel that far. Refuel first!")
            else:
                distance += travel_distance
                fuel -= travel_fuel

                damage_chance = random.randint(1, 100)
                if damage_chance < 30:
                    damage = random.randint(1, 20)
                    print("Your spaceship has taken {} damage!".format(damage))
                    health -= damage

        elif action == '2':
            fuel += random.randint(10, 20)
            print("Refueling...")

        elif action == '3':
            print("Game over. Thanks for playing!")
            break

        else:
            print("Invalid input. Please try again.")

    if health <= 0:
        print("Your spaceship has been destroyed. Game over!")
    elif fuel <= 0:
        print("Your spaceship has run out of fuel. Game over!")
    else:
        print("Congratulations, you have reached your destination {} light years away!".format(distance))

if __name__ == "__main__":
    main()

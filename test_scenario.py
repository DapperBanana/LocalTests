
import random

def explore_planet():
    print("You land on a new planet!")
    resources = random.randint(1, 100)
    print(f"You found {resources} resources on this planet.")
    return resources

def upgrade_ship(ship, resources):
    ship["fuel"] += random.randint(1, 10)
    ship["armor"] += random.randint(1, 5)
    ship["weapons"] += random.randint(1, 5)
    resources -= 50
    print("Your ship has been upgraded!")
    return ship, resources

ship = {
    "fuel": 50,
    "armor": 10,
    "weapons": 10
}

resources = 100

print("Welcome to the Space Exploration Game!")
print("You have a spaceship with some basic resources. Your goal is to explore new planets and upgrade your ship.")

while True:
    option = input("Do you want to explore a new planet? (yes/no): ")

    if option.lower() == "yes":
        resources_found = explore_planet()
        resources += resources_found
    else:
        print("You decided to stay put and not explore any more planets.")
        break

    upgrade_option = input("Do you want to upgrade your ship? (yes/no): ")

    if upgrade_option.lower() == "yes" and resources >= 50:
        ship, resources = upgrade_ship(ship, resources)
    elif resources < 50:
        print("You don't have enough resources to upgrade your ship.")
    else:
        print("You decided not to upgrade your ship.")

    print(f"Current ship stats: Fuel: {ship['fuel']}, Armor: {ship['armor']}, Weapons: {ship['weapons']}")
    print(f"Current resources: {resources}\n")

print("Game over. Thanks for playing!")

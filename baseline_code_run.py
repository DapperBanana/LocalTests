
import random

class Spaceship:
    def __init__(self, name, hull_health, shields, firepower):
        self.name = name
        self.hull_health = hull_health
        self.shields = shields
        self.firepower = firepower

    def attack(self, enemy_ship):
        if self.firepower > enemy_ship.shields:
            damage = self.firepower - enemy_ship.shields
            enemy_ship.hull_health -= damage
            print(f"{self.name} attacks {enemy_ship.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack was blocked by {enemy_ship.name}'s shields!")

def main():
    player_ship = Spaceship("Player Ship", 100, 20, 30)
    enemy_ship = Spaceship("Enemy Ship", 80, 15, 25)

    print("Welcome to the Spaceship Game!")
    print(f"You are piloting the {player_ship.name}. Your enemy is the {enemy_ship.name}.")

    while player_ship.hull_health > 0 and enemy_ship.hull_health > 0:
        player_ship.attack(enemy_ship)
        enemy_ship.attack(player_ship)

        if player_ship.hull_health <= 0:
            print("Your ship has been destroyed! Game over.")
            break
        elif enemy_ship.hull_health <= 0:
            print(f"You have defeated the enemy ship {enemy_ship.name}! You win!")
            break

if __name__ == "__main__":
    main()

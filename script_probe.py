
import random

class Spaceship:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self):
        return random.randint(10, 20)

    def take_damage(self, damage):
        self.health -= damage

def main():
    player_name = input("Enter your spaceship's name: ")
    player_spaceship = Spaceship(player_name)
    enemy_spaceship = Spaceship("Enemy")

    print(f"Welcome to the Spaceship Battle! {player_name} vs Enemy")

    while player_spaceship.health > 0 and enemy_spaceship.health > 0:
        player_attack = player_spaceship.attack()
        enemy_attack = enemy_spaceship.attack()

        enemy_spaceship.take_damage(player_attack)
        player_spaceship.take_damage(enemy_attack)

        print(f"{player_name} attacks Enemy for {player_attack} damage. Enemy health: {enemy_spaceship.health}")
        print(f"Enemy attacks {player_name} for {enemy_attack} damage. {player_name} health: {player_spaceship.health}")

    if player_spaceship.health > 0:
        print(f"Congratulations! {player_name} wins the battle!")
    else:
        print("Game Over! Enemy wins the battle!")

if __name__ == "__main__":
    main()

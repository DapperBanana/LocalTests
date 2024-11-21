
import random

class Spaceship:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.shield = 50
        self.attack = 20

    def take_damage(self, damage):
        if self.shield > 0:
            self.shield -= damage
            if self.shield < 0:
                self.health += self.shield
                self.shield = 0
        else:
            self.health -= damage

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self):
        return random.randint(1, self.attack)

    def status(self):
        print(f"{self.name}'s Health: {self.health}")
        print(f"{self.name}'s Shield: {self.shield}")

def main():
    player_name = input("Enter your spaceship's name: ")
    enemy_name = "Alien Spaceship"
    player = Spaceship(player_name)
    enemy = Spaceship(enemy_name)

    while player.is_alive() and enemy.is_alive():
        player_attack = player.attack_enemy()
        enemy_attack = enemy.attack_enemy()

        print(f"{player_name} attacks {enemy_name} for {player_attack} damage")
        enemy.take_damage(player_attack)
        print(f"{enemy_name} attacks {player_name} for {enemy_attack} damage")
        player.take_damage(enemy_attack)

        player.status()
        enemy.status()

    if player.is_alive():
        print("Congratulations! You have defeated the Alien Spaceship.")
    else:
        print("Game over. The Alien Spaceship has defeated you.")

if __name__ == "__main__":
    main()

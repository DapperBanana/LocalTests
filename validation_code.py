
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.inventory = []

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage

    def heal(self, amount):
        self.hp += amount

    def attack_enemy(self):
        return self.attack + random.randint(-3, 3)

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage

    def attack_player(self):
        return self.attack + random.randint(-2, 2)

def print_status(player, enemy):
    print(f"{player.name} HP: {player.hp}")
    print(f"{enemy.name} HP: {enemy.hp}")

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    enemy = Enemy("Goblin", 50, 5)

    print("Welcome to the RPG game!")

    while player.is_alive() and enemy.is_alive():
        print_status(player, enemy)
        action = input("Do you want to attack (a) or heal (h)? ")

        if action == 'a':
            enemy_damage = player.attack_enemy()
            enemy.take_damage(enemy_damage)
            print(f"You attack the {enemy.name} for {enemy_damage} damage!")

            player_damage = enemy.attack_player()
            player.take_damage(player_damage)
            print(f"The {enemy.name} attacks you for {player_damage} damage!")
        elif action == 'h':
            player.heal(10)
            print("You heal yourself for 10 HP!")

    if player.is_alive():
        print("You defeated the enemy!")
    else:
        print("Game over. You were defeated by the enemy.")

if __name__ == "__main__":
    main()

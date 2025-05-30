
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.coins = 0

    def take_damage(self, damage):
        self.health -= damage

    def deal_damage(self, enemy):
        damage = self.attack - enemy.defense
        if damage < 0:
            damage = 0
        enemy.take_damage(damage)
        print(f"{self.name} dealt {damage} damage to the enemy.")

    def is_alive(self):
        return self.health > 0

class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage

    def deal_damage(self, player):
        damage = self.attack - player.defense
        if damage < 0:
            damage = 0
        player.take_damage(damage)
        print(f"The enemy dealt {damage} damage to {player.name}.")

    def is_alive(self):
        return self.health > 0

def combat(player, enemy):
    while player.is_alive() and enemy.is_alive():
        player.deal_damage(enemy)
        if enemy.is_alive():
            enemy.deal_damage(player)
    if player.is_alive():
        player.coins += random.randint(1, 10)
        print(f"{player.name} defeated the enemy and earned some coins! Total coins: {player.coins}")
    else:
        print(f"{player.name} was defeated by the enemy. Game over.")

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    goblin = Enemy("Goblin", 50, 5, 2)

    print("A wild Goblin appears! Prepare for battle...")
    combat(player, goblin)

if __name__ == "__main__":
    main()

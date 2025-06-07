
import random

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def take_damage(self, damage):
        self.hp -= damage

player_hp = 100
player_attack = 10

enemy = Enemy("Goblin", 50, 5)

print("You have encountered a", enemy.name)

while player_hp > 0 and enemy.hp > 0:
    print("Your HP:", player_hp)
    print(enemy.name, "HP:", enemy.hp)
    print("1. Attack")
    print("2. Run")

    choice = input("Enter your choice: ")

    if choice == "1":
        player_damage = random.randint(player_attack - 3, player_attack + 3)
        print("You attack the", enemy.name, "for", player_damage, "damage.")
        enemy.take_damage(player_damage)

        enemy_damage = random.randint(enemy.attack - 2, enemy.attack + 2)
        print("The", enemy.name, "attacks you for", enemy_damage, "damage.")
        player_hp -= enemy_damage

    elif choice == "2":
        print("You run away from the battle.")
        break

if player_hp <= 0:
    print("You have been defeated. Game over.")
elif enemy.hp <= 0:
    print("You have defeated the", enemy.name, "and emerged victorious!")

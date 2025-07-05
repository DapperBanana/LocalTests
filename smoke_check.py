
import random

# Player class
class Player:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack(self):
        return random.randint(1, self.atk)

# Enemy class
class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack(self):
        return random.randint(1, self.atk)

# Battle function
def battle(player, enemy):
    print(f"{player.name} vs {enemy.name}!\n")

    while player.hp > 0 and enemy.hp > 0:
        player_dmg = player.attack()
        print(f"{player.name} attacks {enemy.name} and deals {player_dmg} damage!")
        enemy.hp -= player_dmg
        print(f"{enemy.name}'s HP: {enemy.hp}\n")

        if enemy.hp <= 0:
            print(f"{player.name} wins the battle!")
            break

        enemy_dmg = enemy.attack()
        print(f"{enemy.name} attacks {player.name} and deals {enemy_dmg} damage!")
        player.hp -= enemy_dmg
        print(f"{player.name}'s HP: {player.hp}\n")

        if player.hp <= 0:
            print(f"{enemy.name} wins the battle!")
            break

# Main function
def main():
    player = Player("Hero", 20, 5)
    enemy = Enemy("Goblin", 10, 3)

    battle(player, enemy)

if __name__ == "__main__":
    main()

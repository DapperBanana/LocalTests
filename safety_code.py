
import random

player_cards = {
    "Warrior": {"attack": 10, "defense": 5},
    "Mage": {"attack": 8, "defense": 3},
    "Archer": {"attack": 6, "defense": 2}
}

enemy_cards = {
    "Orc": {"attack": 8, "defense": 4},
    "Goblin": {"attack": 6, "defense": 2},
    "Troll": {"attack": 10, "defense": 6}
}

player_hp = 50
enemy_hp = 50

player_card = random.choice(list(player_cards.keys()))
enemy_card = random.choice(list(enemy_cards.keys()))

print(f"Player card: {player_card}")
print(f"Enemy card: {enemy_card}")

while player_hp > 0 and enemy_hp > 0:
    player_attack = player_cards[player_card]["attack"]
    player_defense = player_cards[player_card]["defense"]
    enemy_attack = enemy_cards[enemy_card]["attack"]
    enemy_defense = enemy_cards[enemy_card]["defense"]

    player_hp -= max(enemy_attack - player_defense, 0)
    enemy_hp -= max(player_attack - enemy_defense, 0)

    print(f"Player HP: {player_hp}")
    print(f"Enemy HP: {enemy_hp}")

if player_hp <= 0:
    print("You lose!")
else:
    print("You win!")


import random

class Card:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self):
        card_names = ['Fire Dragon', 'Water Leviathan', 'Earth Golem', 'Wind Griffin']
        card = Card(random.choice(card_names), random.randint(1, 10), random.randint(1, 10))
        self.hand.append(card)

    def play_card(self):
        if not self.hand:
            print(f"{self.name}'s hand is empty!")
            return
        card = random.choice(self.hand)
        print(f"{self.name} plays {card.name} (Attack: {card.attack}, Defense: {card.defense})")
        self.hand.remove(card)

# Game setup
player1 = Player('Player 1')
player2 = Player('Player 2')

# Draw initial cards
for _ in range(5):
    player1.draw_card()
    player2.draw_card()

# Play cards
for _ in range(3):
    player1.play_card()
    player2.play_card()

print("Game Over!")

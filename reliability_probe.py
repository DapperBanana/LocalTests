
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
        card = Card("Card", random.randint(1, 10), random.randint(1, 10))
        self.hand.append(card)
        print(f"{self.name} drew a card with attack: {card.attack} and defense: {card.defense}")

    def play_card(self):
        if len(self.hand) == 0:
            print(f"{self.name} has no cards to play!")
            return

        card = self.hand.pop(0)
        print(f"{self.name} played {card.name} with attack: {card.attack} and defense: {card.defense}")

    def show_hand(self):
        print(f"{self.name}'s hand:")
        for card in self.hand:
            print(f"{card.name} - Attack: {card.attack}, Defense: {card.defense}")

# Main game loop
player1 = Player("Player 1")
player2 = Player("Player 2")

for _ in range(5):
    player1.draw_card()
    player2.draw_card()

player1.show_hand()
player2.show_hand()

player1.play_card()
player2.play_card()

player1.show_hand()
player2.show_hand()

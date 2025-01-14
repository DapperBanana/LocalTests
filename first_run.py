
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
        card = Card(f"Card {len(self.hand) + 1}", random.randint(1, 10), random.randint(1, 10))
        self.hand.append(card)
        print(f"{self.name} drew a card: {card.name} (Attack: {card.attack}, Defense: {card.defense})")

def battle(player1, player2):
    print(f"Battle between {player1.name} and {player2.name}!")
    for i in range(min(len(player1.hand), len(player2.hand))):
        card1 = player1.hand[i]
        card2 = player2.hand[i]
        print(f"{player1.name}'s {card1.name} (Attack: {card1.attack}, Defense: {card1.defense}) vs {player2.name}'s {card2.name} (Attack: {card2.attack}, Defense: {card2.defense})")
        if card1.attack > card2.defense:
            print(f"{player1.name} wins this round!")
        elif card2.attack > card1.defense:
            print(f"{player2.name} wins this round!")
        else:
            print("It's a tie!")

# Main game loop
player1 = Player("Player 1")
player2 = Player("Player 2")

for _ in range(5):
    player1.draw_card()
    player2.draw_card()

battle(player1, player2)


import random

class Card:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

class Player:
    def __init__(self):
        self.hand = []

    def draw_card(self):
        card = Card("Goblin", random.randint(1, 5), random.randint(1, 5))
        self.hand.append(card)
    
    def show_hand(self):
        for card in self.hand:
            print(f"{card.name} - Attack: {card.attack}, Defense: {card.defense}")

def battle(player1, player2):
    for card1, card2 in zip(player1.hand, player2.hand):
        if card1.attack > card2.defense:
            print(f"{card1.name} wins against {card2.name}!")
        elif card1.attack < card2.defense:
            print(f"{card2.name} wins against {card1.name}!")
        else:
            print(f"{card1.name} and {card2.name} draw!")

player1 = Player()
player2 = Player()

for _ in range(3):
    player1.draw_card()
    player2.draw_card()

print("Player 1's hand:")
player1.show_hand()

print("\nPlayer 2's hand:")
player2.show_hand()

print("\nBattle results:")
battle(player1, player2)

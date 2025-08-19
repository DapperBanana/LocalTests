
import random

class Card:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} - Attack: {self.attack}, Defense: {self.defense}"

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def draw_card(self):
        name = input("Enter card name: ")
        attack = int(input("Enter card attack value: "))
        defense = int(input("Enter card defense value: "))
        card = Card(name, attack, defense)
        self.hand.append(card)

    def play_card(self):
        if not self.hand:
            print("No cards in hand!")
            return
        
        print("Your hand:")
        for i, card in enumerate(self.hand):
            print(f"{i+1}. {card}")

        choice = int(input("Choose a card to play: ")) - 1
        card = self.hand.pop(choice)
        return card

    def calculate_score(self, card):
        self.score += card.attack + card.defense

    def display_score(self):
        print(f"Player {self.name} score: {self.score}")

player1 = Player("A")
player2 = Player("B")

for _ in range(2):
    player1.draw_card()
    player2.draw_card()

for _ in range(3):
    card1 = player1.play_card()
    card2 = player2.play_card()

    if card1.attack > card2.defense:
        player1.calculate_score(card1)
    if card2.attack > card1.defense:
        player2.calculate_score(card2)

player1.display_score()
player2.display_score()

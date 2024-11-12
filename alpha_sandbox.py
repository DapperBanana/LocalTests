
import random

class Card:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.health = 100
        self.deck = deck
        self.hand = []

    def draw_card(self):
        card = random.choice(deck)
        self.hand.append(card)
        print(f"{self.name} draws {card.name}")

    def play_card(self, card_index, opponent):
        card = self.hand.pop(card_index)
        print(f"{self.name} plays {card.name}")
        if card.attack > opponent.hand[0].defense:
            print(f"{self.name} deals {card.attack} damage to {opponent.name}")
            opponent.health -= card.attack
        else:
            print(f"{self.name}'s attack is blocked by {opponent.name}'s card")
        print(f"{opponent.name}'s health: {opponent.health}")

# Create some cards
card1 = Card("Dragon", 10, 5)
card2 = Card("Goblin", 5, 2)
card3 = Card("Wizard", 8, 3)

# Create two players with their decks
deck = [card1, card2, card3]
player1 = Player("Player 1", deck.copy())
player2 = Player("Player 2", deck.copy())

# Shuffle decks
random.shuffle(player1.deck)
random.shuffle(player2.deck)

# Game loop
while player1.health > 0 and player2.health > 0:
    player1.draw_card()
    player2.draw_card()

    player1.play_card(0, player2)
    player2.play_card(0, player1)

print("Game over")
if player1.health <= 0:
    print("Player 2 wins!")
else:
    print("Player 1 wins!")

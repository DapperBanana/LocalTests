
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
        self.health = 100
        self.hand = []

    def draw_card(self):
        card = random.choice(deck)
        self.hand.append(card)

    def play_card(self, card_index):
        card = self.hand.pop(card_index)
        return card

# Create some cards
card1 = Card("Warrior", 10, 5)
card2 = Card("Mage", 5, 10)
card3 = Card("Archer", 8, 7)

# Create a deck of cards
deck = [card1, card2, card3]

# Create two players
player1 = Player("Player 1")
player2 = Player("Player 2")

# Draw initial hand for both players
player1.draw_card()
player1.draw_card()
player2.draw_card()
player2.draw_card()

while player1.health > 0 and player2.health > 0:
    print(f"{player1.name} Health: {player1.health}")
    print(f"{player2.name} Health: {player2.health}")

    print(f"{player1.name}'s Hand:")
    for i, card in enumerate(player1.hand):
        print(f"{i+1}. {card}")

    choice = int(input("Select a card to play (1-3): ")) - 1
    player1_card = player1.play_card(choice)

    player2_card = random.choice(player2.hand)

    print(f"{player1.name} plays {player1_card.name}")
    print(f"{player2.name} plays {player2_card.name}")

    if player1_card.attack > player2_card.defense:
        player2.health -= (player1_card.attack - player2_card.defense)
    elif player1_card.attack < player2_card.defense:
        player1.health -= (player2_card.defense - player1_card.attack)

print("Game over!")
if player1.health <= 0:
    print(f"{player2.name} wins!")
elif player2.health <= 0:
    print(f"{player1.name} wins!")

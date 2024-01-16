
import random

class Card:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} (Attack: {self.attack}, Defense: {self.defense})"

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []

    def add_card(self, card):
        self.deck.append(card)

    def draw_card(self):
        return self.deck.pop(random.randint(0, len(self.deck)-1))

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        print(f"{self.player1.name} and {self.player2.name} are playing...")
        print("------------------------------")
        
        # Draw initial cards
        self.player1_card = self.player1.draw_card()
        self.player2_card = self.player2.draw_card()
        
        print(f"{self.player1.name} plays {self.player1_card}")
        print(f"{self.player2.name} plays {self.player2_card}")
        print("------------------------------")

        # Compare attack and defense values
        if self.player1_card.attack > self.player2_card.defense:
            print(f"{self.player1.name} wins!")
        elif self.player2_card.attack > self.player1_card.defense:
            print(f"{self.player2.name} wins!")
        else:
            print("It's a tie!")
        
        print("------------------------------")

# Create some cards
card1 = Card("Card 1", 5, 3)
card2 = Card("Card 2", 4, 6)
card3 = Card("Card 3", 7, 2)

# Create players and add cards to their decks
player1 = Player("Player 1")
player1.add_card(card1)
player1.add_card(card2)

player2 = Player("Player 2")
player2.add_card(card3)

# Create a game and play
game = Game(player1, player2)
game.play()

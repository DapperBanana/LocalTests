
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
        self.deck = []
        self.health = 100
        self.mana = 0

    def draw_card(self):
        if len(self.deck) > 0:
            card = self.deck.pop(0)
            self.hand.append(card)
            print(f"{self.name} drew {card.name}")
        else:
            print("No cards left in deck!")

    def play_card(self, card_idx):
        if card_idx < len(self.hand):
            card = self.hand.pop(card_idx)
            self.mana -= 1
            return card
        else:
            print("Invalid card index!")
            return None

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = random.choice([player1, player2])

    def start(self):
        while self.player1.health > 0 and self.player2.health > 0:
            print(f"{self.turn.name}'s turn")
            self.turn.draw_card()
            card_idx = random.randint(0, len(self.turn.hand)-1)
            card = self.turn.play_card(card_idx)
            
            if card:
                print(f"{self.turn.name} played {card.name} - Attack: {card.attack}, Defense: {card.defense}")
                
                opponent = self.player2 if self.turn == self.player1 else self.player1
                opponent.health -= card.attack
                print(f"{opponent.name}'s health: {opponent.health}")
                
            self.turn = self.player1 if self.turn == self.player2 else self.player2

        winner = self.player1 if self.player1.health > 0 else self.player2
        print(f"{winner.name} wins the game!")

# Create some cards
card1 = Card("Dragon", 10, 5)
card2 = Card("Goblin", 3, 2)
card3 = Card("Knight", 7, 8)

# Create players and decks
player1 = Player("Player 1")
player1.deck = [card1, card2, card3, card3, card1]
player2 = Player("Player 2")
player2.deck = [card2, card3, card2, card1, card3]

# Start the game
game = Game(player1, player2)
game.start()


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
        card_name = input("Enter the name of the card you want to draw: ")
        attack = random.randint(1, 10)
        defense = random.randint(1, 10)
        card = Card(card_name, attack, defense)
        self.hand.append(card)
        print(f"{self.name} drew a card: {card_name}")

    def play_card(self):
        print(f"{self.name}'s Hand:")
        for idx, card in enumerate(self.hand):
            print(f"{idx + 1}. {card.name} ({card.attack}/{card.defense})")
        
        choice = int(input("Enter the number of the card you want to play: ")) - 1
        played_card = self.hand.pop(choice)
        print(f"{self.name} played {played_card.name} ({played_card.attack}/{played_card.defense})")

class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def run_game(self):
        for player in self.players:
            print(f"{player.name}'s turn:")
            player.draw_card()
            player.play_card()

# Create players
player1 = Player("Alice")
player2 = Player("Bob")

# Create a game
game = Game()

# Add players to the game
game.add_player(player1)
game.add_player(player2)

# Run the game
game.run_game()

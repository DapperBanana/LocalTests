
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
        card_names = ["Goblin", "Dragon", "Wizard", "Knight"]
        card = Card(random.choice(card_names), random.randint(1, 10), random.randint(1, 10))
        self.hand.append(card)

    def play_card(self):
        if len(self.hand) > 0:
            return self.hand.pop(random.randint(0, len(self.hand)-1))
        else:
            return None

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start(self):
        while self.player1.health > 0 and self.player2.health > 0:
            self.player1.draw_card()
            self.player2.draw_card()

            print(f"{self.player1.name}'s turn:")
            card1 = self.player1.play_card()
            if card1:
                print(f"{self.player1.name} plays {card1}")
                print(f"{self.player2.name}'s health is now {self.player2.health - card1.attack}")
                self.player2.health -= card1.attack

            print(f"{self.player2.name}'s turn:")
            card2 = self.player2.play_card()
            if card2:
                print(f"{self.player2.name} plays {card2}")
                print(f"{self.player1.name}'s health is now {self.player1.health - card2.attack}")
                self.player1.health -= card2.attack

        if self.player1.health <= 0:
            print(f"{self.player2.name} wins!")
        else:
            print(f"{self.player1.name} wins!")

# Create players
player1 = Player("Player 1")
player2 = Player("Player 2")

# Create game
game = Game(player1, player2)

# Start game
game.start()

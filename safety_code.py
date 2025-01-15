
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
        card = Card("Card" + str(len(self.hand) + 1), random.randint(1, 10), random.randint(1, 10))
        self.hand.append(card)
        print(f"{self.name} drew a new card: {card.name}")

    def play_card(self):
        if len(self.hand) == 0:
            print(f"{self.name}'s hand is empty!")
            return
        
        card = self.hand.pop(0)
        print(f"{self.name} played {card.name} with attack {card.attack} and defense {card.defense}")

def battle(player1, player2):
    player1.draw_card()
    player2.draw_card()

    p1_card = player1.hand[0]
    p2_card = player2.hand[0]

    print(f"{player1.name}'s card: {p1_card.name} - Attack: {p1_card.attack}, Defense: {p1_card.defense}")
    print(f"{player2.name}'s card: {p2_card.name} - Attack: {p2_card.attack}, Defense: {p2_card.defense}")

    if p1_card.attack > p2_card.defense:
        print(f"{player1.name} wins the battle!")
    elif p2_card.attack > p1_card.defense:
        print(f"{player2.name} wins the battle!")
    else:
        print("It's a tie!")

# Create players
player1 = Player("Player 1")
player2 = Player("Player 2")

# Play the game
battle(player1, player2)

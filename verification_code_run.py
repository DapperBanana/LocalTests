
import random

class Card:
    def __init__(self, name, power, defense):
        self.name = name
        self.power = power
        self.defense = defense

    def __str__(self):
        return f"{self.name} (Power: {self.power}, Defense: {self.defense})"


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self):
        cards = [
            Card("Goblin", 2, 1),
            Card("Dragon", 5, 3),
            Card("Knight", 3, 2),
            Card("Wizard", 4, 2),
        ]
        card = random.choice(cards)
        self.hand.append(card)

    def show_hand(self):
        print(f"{self.name}'s Hand:")
        for card in self.hand:
            print(card)

    def play_card(self, card_index):
        return self.hand.pop(card_index)


def battle(player1, player2):
    player1.draw_card()
    player2.draw_card()
    player1.show_hand()
    player2.show_hand()

    player1_card_index = int(input(f"{player1.name}, choose a card to play (0-{len(player1.hand)-1}): "))
    player2_card_index = int(input(f"{player2.name}, choose a card to play (0-{len(player2.hand)-1}): "))

    player1_card = player1.play_card(player1_card_index)
    player2_card = player2.play_card(player2_card_index)

    if player1_card.power > player2_card.defense:
        print(f"{player1.name} wins the battle!")
    elif player2_card.power > player1_card.defense:
        print(f"{player2.name} wins the battle!")
    else:
        print("It's a tie!")

# Create two players
player1 = Player("Player 1")
player2 = Player("Player 2")

# Start the game
while True:
    battle(player1, player2)
    continue_game = input("Do you want to continue playing? (yes/no): ")
    if continue_game.lower() != 'yes':
        break

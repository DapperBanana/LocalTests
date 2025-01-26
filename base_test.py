
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
        cards = [
            Card("Goblin", 2, 1),
            Card("Wizard", 3, 2),
            Card("Dragon", 5, 4)
        ]
        card = random.choice(cards)
        self.hand.append(card)
        print(f"{self.name} drew a {card.name}!")

    def display_hand(self):
        print(f"{self.name}'s hand:")
        for card in self.hand:
            print(f"{card.name} - Attack: {card.attack} Defense: {card.defense}")

def battle(player1, player2):
    player1.draw_card()
    player2.draw_card()
    player1.display_hand()
    player2.display_hand()

    # Simple battle logic: compare attack values
    if player1.hand[0].attack > player2.hand[0].defense:
        print(f"{player1.name} wins the battle!")
    elif player2.hand[0].attack > player1.hand[0].defense:
        print(f"{player2.name} wins the battle!")
    else:
        print("It's a tie!")

# Main game loop
player1 = Player("Player 1")
player2 = Player("Player 2")

while True:
    battle(player1, player2)
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break

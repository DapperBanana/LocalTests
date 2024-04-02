
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

    def draw_card(self):
        card = Card("Card" + str(len(self.hand) + 1), random.randint(1, 10), random.randint(1, 10))
        self.hand.append(card)
        print(f"{self.name} drew a card: {card}")

    def play_card(self, card_index):
        if card_index < 1 or card_index > len(self.hand):
            print("Invalid card index")
        else:
            card = self.hand.pop(card_index - 1)
            print(f"{self.name} played the card: {card}")
            return card

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start(self):
        for _ in range(3):
            self.player1.draw_card()
            self.player2.draw_card()

        for _ in range(3):
            print("Player 1's turn")
            card_index = int(input("Choose a card to play (1-3): "))
            card1 = self.player1.play_card(card_index)

            print("Player 2's turn")
            card2 = random.choice(self.player2.hand)
            print(f"Player 2 played the card: {card2}")
            self.player2.hand.remove(card2)

            if card1.attack > card2.defense:
                print("Player 1 wins the round!")
            elif card1.attack < card2.defense:
                print("Player 2 wins the round!")
            else:
                print("It's a tie!")

if __name__ == "__main__":
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    game = Game(player1, player2)
    game.start()

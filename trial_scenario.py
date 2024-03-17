
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
        self.points = 0

    def draw_card(self):
        card = Card("Card", random.randint(1, 10), random.randint(1, 10))
        self.hand.append(card)

    def play_card(self):
        if not self.hand:
            print("You have no cards to play!")
            return

        card = self.hand.pop()
        return card

    def calculate_points(self, card):
        self.points += card.attack + card.defense

def battle(player1, player2):
    card1 = player1.play_card()
    card2 = player2.play_card()

    player1.calculate_points(card1)
    player2.calculate_points(card2)

    print(f"{player1.name} played {card1.name} with attack {card1.attack} and defense {card1.defense}")
    print(f"{player2.name} played {card2.name} with attack {card2.attack} and defense {card2.defense}")

    if card1.attack + card1.defense > card2.attack + card2.defense:
        print(f"{player1.name} wins this round!")
    elif card1.attack + card1.defense < card2.attack + card2.defense:
        print(f"{player2.name} wins this round!")
    else:
        print("It's a tie!")

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    for i in range(5):
        player1.draw_card()
        player2.draw_card()

    for i in range(5):
        print(f"Round {i+1}")
        battle(player1, player2)

    print(f"Final scores:")
    print(f"{player1.name}: {player1.points} points")
    print(f"{player2.name}: {player2.points} points")

if __name__ == "__main__":
    main()


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
        self.hand = []
        self.points = 0

    def draw_card(self):
        if len(self.deck) == 0:
            print("No cards left in the deck!")
            return
        card = self.deck.pop()
        self.hand.append(card)
        print(f"{self.name} drew {card}.")

    def play_card(self):
        if len(self.hand) == 0:
            print("No cards in hand!")
            return
        card = random.choice(self.hand)
        self.hand.remove(card)
        print(f"{self.name} played {card}.")
        return card

    def calculate_points(self):
        self.points = sum(card.attack for card in self.hand)
        return self.points


def main():
    card1 = Card("Dragon", 10, 5)
    card2 = Card("Knight", 7, 8)
    card3 = Card("Goblin", 4, 2)
    card4 = Card("Wizard", 6, 3)

    player1 = Player("Player 1")
    player1.deck = [card1, card2, card3, card4]

    player2 = Player("Player 2")
    player2.deck = [card1, card2, card3, card4]

    # Play the game
    while True:
        player1.draw_card()
        player2.draw_card()

        player1_points = player1.calculate_points()
        player2_points = player2.calculate_points()

        if player1_points > player2_points:
            print(f"{player1.name} wins this round!")
            player1.points += 1
        elif player1_points < player2_points:
            print(f"{player2.name} wins this round!")
            player2.points += 1
        else:
            print("It's a tie!")

        print(f"{player1.name}'s points: {player1.points}")
        print(f"{player2.name}'s points: {player2.points}")

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break

    print("Game over!")
    print(f"{player1.name}'s final points: {player1.points}")
    print(f"{player2.name}'s final points: {player2.points}")

if __name__ == '__main__':
    main()

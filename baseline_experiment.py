
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
        self.health = 100

    def draw_card(self):
        card = Card("Card" + str(len(self.hand) + 1), random.randint(1, 10), random.randint(1, 10))
        self.hand.append(card)
        print(f"{self.name} drew {card.name} ({card.attack}/{card.defense})")

    def play_card(self, card_index, opponent):
        if card_index < 0 or card_index >= len(self.hand):
            print("Invalid card index")
            return
        
        card = self.hand.pop(card_index)
        print(f"{self.name} played {card.name} ({card.attack}/{card.defense})")

        opponent.defense -= card.attack
        print(f"{opponent.name} defended with {opponent.defense} health")

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    while player1.health > 0 and player2.health > 0:
        player1.draw_card()
        player2.draw_card()

        player1_index = random.randint(0, len(player1.hand) - 1)
        player2_index = random.randint(0, len(player2.hand) - 1)

        player1.play_card(player1_index, player2)
        player2.play_card(player2_index, player1)

    if player1.health <= 0:
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")

if __name__ == "__main__":
    main()

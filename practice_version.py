
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
        card = Card("Card", random.randint(1, 10), random.randint(1, 10))
        self.hand.append(card)

    def play_card(self, card_index):
        return self.hand.pop(card_index)

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    for i in range(5):
        player1.draw_card()
        player2.draw_card()

    while len(player1.hand) > 0 and len(player2.hand) > 0:
        print("Player 1's Turn")
        print("Player 1's Hand:")
        for i, card in enumerate(player1.hand):
            print(f"{i+1}. {card.name} - Attack: {card.attack}, Defense: {card.defense}")
        
        chosen_card_index = int(input("Choose a card to play (1-5): ")) - 1
        player1_card = player1.play_card(chosen_card_index)
        
        print(f"Player 1 played {player1_card.name} - Attack: {player1_card.attack}, Defense: {player1_card.defense}")

        print()
        print("Player 2's Turn")
        print("Player 2's Hand:")
        for i, card in enumerate(player2.hand):
            print(f"{i+1}. {card.name} - Attack: {card.attack}, Defense: {card.defense}")

        player2_card = player2.play_card(random.randint(0, len(player2.hand) - 1))
        
        print(f"Player 2 played {player2_card.name} - Attack: {player2_card.attack}, Defense: {player2_card.defense}")

        if player1_card.attack > player2_card.defense:
            print("Player 1 wins this round!")
        elif player2_card.attack > player1_card.defense:
            print("Player 2 wins this round!")
        else:
            print("It's a draw!")

    if len(player1.hand) > 0:
        print("Player 1 wins the game!")
    else:
        print("Player 2 wins the game!")

if __name__ == "__main__":
    main()

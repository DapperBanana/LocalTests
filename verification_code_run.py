
import random

class Card:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
        
    def __str__(self):
        return f"{self.name} (A: {self.attack}, D: {self.defense})"

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        
    def draw_card(self, deck):
        card = random.choice(deck)
        self.cards.append(card)
        deck.remove(card)
        
    def play_card(self, index, opponent):
        card = self.cards[index]
        print(f"{self.name} plays {card}!")
        if card.attack > opponent.cards[index].defense:
            print(f"{self.name} wins the round!")
        elif card.attack < opponent.cards[index].defense:
            print(f"{opponent.name} wins the round!")
        else:
            print("It's a tie!")
    
    def show_hand(self):
        print(f"{self.name}'s hand:")
        for i, card in enumerate(self.cards):
            print(f"{i+1}. {card}")
        
def create_deck():
    deck = []
    deck.append(Card("Goblin", 1, 1))
    deck.append(Card("Dragon", 3, 2))
    deck.append(Card("Knight", 2, 3))
    deck.append(Card("Wizard", 1, 4))
    return deck

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    opponent = Player("Computer")
    deck = create_deck()
    
    # Draw initial cards
    for _ in range(3):
        player.draw_card(deck)
        opponent.draw_card(deck)
    
    while True:
        print("\n-------------------")
        print(f"{player.name}'s turn")
        
        player.show_hand()
        card_index = int(input("Select a card to play (1-3): ")) - 1
        player.play_card(card_index, opponent)
        
        # Check if the game is over
        if len(deck) == 0:
            print("No more cards left. Game over!")
            break
        
        player.draw_card(deck)
        opponent.draw_card(deck)
        
if __name__ == "__main__":
    main()

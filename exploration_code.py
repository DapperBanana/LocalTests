
import random

class Card:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
    
    def __str__(self):
        return f"{self.name} (ATK: {self.attack}, DEF: {self.defense})"

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def draw_card(self):
        new_card = Card(f"Card {len(self.hand)+1}", random.randint(1, 10), random.randint(1, 10))
        self.hand.append(new_card)
    
    def show_hand(self):
        print(f"{self.name}'s Hand:")
        for card in self.hand:
            print(card)
    
    def play_card(self, card_index):
        return self.hand.pop(card_index)

def battle(player1, player2):
    player1_card = random.choice(player1.hand)
    player2_card = random.choice(player2.hand)
    
    print(f"{player1.name} plays {player1_card}")
    print(f"{player2.name} plays {player2_card}")
    
    if player1_card.attack > player2_card.defense:
        print(f"{player1.name} wins the round!")
    elif player2_card.attack > player1_card.defense:
        print(f"{player2.name} wins the round!")
    else:
        print("It's a tie!")
    
    player1.hand.remove(player1_card)
    player2.hand.remove(player2_card)

# Main game loop
player1 = Player("Player 1")
player2 = Player("Player 2")

for _ in range(5):
    player1.draw_card()
    player2.draw_card()

player1.show_hand()
player2.show_hand()

for _ in range(5):
    battle(player1, player2)

print("Game over!")

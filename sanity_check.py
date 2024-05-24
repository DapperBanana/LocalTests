
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
        self.active_card = None
        self.score = 0
    
    def play_card(self):
        if len(self.hand) == 0:
            return None
        
        self.active_card = self.hand.pop(random.randint(0, len(self.hand)-1))
        return self.active_card
    
    def calculate_score(self, opponent_card):
        if self.active_card.attack > opponent_card.defense:
            self.score += 1
            print(f"{self.name} wins this round!")
        elif self.active_card.attack < opponent_card.defense:
            print(f"{self.name} loses this round!")
        else:
            print("It's a tie!")
    
    def show_hand(self):
        for i, card in enumerate(self.hand):
            print(f"{i+1}. {card.name} (Attack: {card.attack}, Defense: {card.defense})")
            

def main():
    card1 = Card("Warrior", 5, 3)
    card2 = Card("Mage", 4, 4)
    card3 = Card("Rogue", 3, 5)
    
    player1 = Player("Player 1")
    player1.hand = [card1, card2, card3]
    
    player2 = Player("Player 2")
    player2.hand = [card1, card2, card3]
    
    rounds = 3
    
    for i in range(rounds):
        print(f"Round {i+1}:")
        
        player1.show_hand()
        player1_card = player1.play_card()
        print(f"{player1.name} plays {player1_card.name}")
        
        player2.show_hand()
        player2_card = player2.play_card()
        print(f"{player2.name} plays {player2_card.name}")
        
        player1.calculate_score(player2_card)
    
    print(f"Final Score: {player1.name}: {player1.score}, {player2.name}: {player2.score}")
    
    if player1.score > player2.score:
        print(f"{player1.name} wins!")
    elif player1.score < player2.score:
        print(f"{player2.name} wins!")
    else:
        print("It's a tie!")
        

if __name__ == "__main__":
    main()

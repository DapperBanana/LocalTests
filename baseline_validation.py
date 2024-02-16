
import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
                
    def shuffle(self):
        random.shuffle(self.cards)
        
    def draw_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

def hit(deck, hand):
    hand.add_card(deck.draw_card())
    hand.adjust_for_ace()

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print(f" {dealer.cards[1]}")
    print("\nPlayer's Hand:", *player.cards, sep="\n ")

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n ")
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)

def play_again():
    while True:
        decision = input("\nDo you want to play again? (y/n): ")
        if decision.lower() == 'y':
            return True
        elif decision.lower() == 'n':
            return False
        else:
            print("Please enter 'y' or 'n'.")

def blackjack_game():
    print("Welcome to Blackjack!\n")
    
    while True:
        # Create and shuffle the deck
        deck = Deck()
        deck.shuffle()
        
        # Deal two cards to the player and the dealer
        player_hand = Hand()
        dealer_hand = Hand()
        for _ in range(2):
            player_hand.add_card(deck.draw_card())
            dealer_hand.add_card(deck.draw_card())
        
        # Play the game
        playing = True
        while playing:
            show_some(player_hand, dealer_hand)
            
            # Check if player or dealer has blackjack or has gone over 21
            if player_hand.value == 21:
                print("Player wins with a Blackjack!")
                playing = False
                break
            elif player_hand.value > 21:
                print("Player busts! Dealer wins.")
                playing = False
                break
            elif dealer_hand.value == 21:
                print("Dealer wins with a Blackjack!")
                playing = False
                break
            elif dealer_hand.value > 21:
                print("Dealer busts! Player wins.")
                playing = False
                break
            
            # Ask the player to hit or stand
            while True:
                decision = input("\nDo you want to hit or stand? (h/s): ")
                if decision.lower() == 'h':
                    hit(deck, player_hand)
                    break
                elif decision.lower() == 's':
                    playing = False
                    break
                else:
                    print("Please enter 'h' or 's'.")
        
        # Dealer's turn
        if playing:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
                
            show_all(player_hand, dealer_hand)
            
            # Determine the winner
            if dealer_hand.value > 21:
                print("Dealer busts! Player wins.")
            elif dealer_hand.value > player_hand.value:
                print("Dealer wins.")
            elif dealer_hand.value < player_hand.value:
                print("Player wins.")
            else:
                print("It's a tie!")
        
        if not play_again():
            break

blackjack_game()

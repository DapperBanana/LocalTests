
import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            card = (rank, suit)
            deck.append(card)
    random.shuffle(deck)
    return deck

def get_value(hand):
    value = 0
    aces = 0
    for card in hand:
        if card[0] in ['J', 'Q', 'K']:
            value += 10
        elif card[0] == 'A':
            aces += 1
        else:
            value += int(card[0])
    for _ in range(aces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1
    return value

deck = create_deck()
player_hand = []
dealer_hand = []

player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())

print("Player's hand:")
for card in player_hand:
    print(f"{card[0]} of {card[1]}")

print("Dealer's hand:")
print(f"{dealer_hand[0][0]} of {dealer_hand[0][1]}")
print("")

player_done = False
while not player_done:
    player_value = get_value(player_hand)
    print(f"Your hand value: {player_value}")
    if player_value > 21:
        print("Bust! You lose.")
        player_done = True
    else:
        choice = input("Do you want to hit or stand? (h/s): ")
        if choice.lower() == 'h':
            player_hand.append(deck.pop())
            print(f"You draw: {player_hand[-1][0]} of {player_hand[-1][1]}")
        else:
            player_done = True

dealer_value = get_value(dealer_hand)
while dealer_value < 17:
    dealer_hand.append(deck.pop())
    dealer_value = get_value(dealer_hand)

print("\nDealer's hand:")
for card in dealer_hand:
    print(f"{card[0]} of {card[1]}")
print(f"Dealer's hand value: {dealer_value}")

if dealer_value > 21 or player_value > dealer_value:
    print("You win!")
elif dealer_value > player_value:
    print("Dealer wins!")
else:
    print("It's a tie!")

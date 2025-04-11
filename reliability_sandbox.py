
import random

def create_deck():
    deck = []
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for suit in suits:
        for value in values:
            deck.append((value, suit))
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        if card[0] in ['J', 'Q', 'K']:
            value += 10
        elif card[0] == 'A':
            num_aces += 1
        else:
            value += int(card[0])
    
    for _ in range(num_aces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1
    return value

def print_hand(hand):
    for card in hand:
        print(f'{card[0]} of {card[1]}')

deck = create_deck()
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

print('Player\'s hand:')
print_hand(player_hand)
print('\nDealer\'s hand:')
print(dealer_hand[0][0], 'of', dealer_hand[0][1])
print('\n')

while True:
    player_value = calculate_hand_value(player_hand)
    if player_value == 21:
        print('Blackjack! Player wins!')
        break
    elif player_value > 21:
        print('Bust! Dealer wins!')
        break
    
    action = input('Do you want to hit or stand? (h/s): ')
    if action == 'h':
        player_hand.append(deck.pop())
        print('\nPlayer\'s hand:')
        print_hand(player_hand)
    elif action == 's':
        break

print('\nDealer\'s hand:')
print_hand(dealer_hand)
while calculate_hand_value(dealer_hand) < 17:
    dealer_hand.append(deck.pop())
    print(f'\nDealer hits: {dealer_hand[-1][0]} of {dealer_hand[-1][1]}')
    print_hand(dealer_hand)

dealer_value = calculate_hand_value(dealer_hand)
if dealer_value > 21:
    print('\nDealer busts! Player wins!')
elif player_value > dealer_value:
    print('\nPlayer wins!')
elif player_value < dealer_value:
    print('\nDealer wins!')
else:
    print('\nIt\'s a tie!')


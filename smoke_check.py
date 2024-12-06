
import random

def create_deck():
    deck = []
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    for suit in suits:
        for value in values:
            deck.append(value + ' of ' + suit)
    
    return deck

def get_card_value(card):
    if card[0] in ['J', 'Q', 'K']:
        return 10
    elif card[0] == 'A':
        return 11
    else:
        return int(card.split()[0])

def calculate_hand_value(hand):
    total_value = sum([get_card_value(card) for card in hand])
    
    # Check for aces and adjust their value if needed
    num_aces = hand.count('A')
    while total_value > 21 and num_aces > 0:
        total_value -= 10
        num_aces -= 1
        
    return total_value

def main():
    deck = create_deck()
    random.shuffle(deck)
    
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    print("Your hand:", player_hand, "Value:", player_value)
    print("Dealer's hand:", [dealer_hand[0], 'Unknown'])
    
    # Player's turn
    while True:
        action = input("Do you want to hit or stand? ").lower()
        
        if action == 'hit':
            new_card = deck.pop()
            player_hand.append(new_card)
            player_value = calculate_hand_value(player_hand)
            print("You drew:", new_card, "Value:", player_value)
            
            if player_value > 21:
                print("Bust! You lose.")
                return
        elif action == 'stand':
            break
        else:
            continue
    
    # Dealer's turn
    print("Dealer's hand:", dealer_hand, "Value:", dealer_value)
    
    while dealer_value < 17:
        new_card = deck.pop()
        dealer_hand.append(new_card)
        dealer_value = calculate_hand_value(dealer_hand)
        print("Dealer drew:", new_card, "Value:", dealer_value)
    
    if dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("You lose.")
    else:
        print("It's a tie!")
    
if __name__ == "__main__":
    main()

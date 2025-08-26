
import random

def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

def calculate_score(hand):
    score = 0
    num_aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            score += 10
        elif card == 'A':
            num_aces += 1
        else:
            score += int(card)
    
    for _ in range(num_aces):
        if score + 11 <= 21:
            score += 11
        else:
            score += 1
    
    return score

def blackjack_game():
    player_hand = []
    dealer_hand = []
    
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())
    
    print("Player's hand:", player_hand)
    print("Dealer's hand:", [dealer_hand[0], 'X'])
    
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    
    if player_score == 21:
        print("Player has Blackjack! Player wins.")
        return
    
    while player_score < 21:
        action = input("Enter 'hit' to draw another card or 'stand' to keep current hand: ")
        if action == 'hit':
            player_hand.append(deal_card())
            print("Player's hand:", player_hand)
            player_score = calculate_score(player_hand)
            if player_score > 21:
                print("Player busts! Dealer wins.")
                return
        elif action == 'stand':
            break
    
    print("Dealer's hand:", dealer_hand)
    while dealer_score < 17:
        dealer_hand.append(deal_card())
        print("Dealer's hand:", dealer_hand)
        dealer_score = calculate_score(dealer_hand)
    
    if dealer_score > 21 or player_score > dealer_score:
        print("Player wins!")
    elif player_score < dealer_score:
        print("Dealer wins.")
    else:
        print("It's a tie!")
    
blackjack_game()

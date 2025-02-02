
import random

def get_card_value(card):
    if card.isdigit():
        return int(card)
    elif card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return 10

def calculate_score(cards):
    score = sum([get_card_value(card) for card in cards])
    num_aces = cards.count('A')
    
    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1
    
    return score

def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

def blackjack():
    player_cards = []
    dealer_cards = []
    
    player_cards.append(deal_card())
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())
    
    print(f"Player's cards: {player_cards}")
    print(f"Dealer's cards: {dealer_cards[0]}")
    
    player_score = calculate_score(player_cards)
    
    while player_score < 21:
        action = input("Do you want to hit or stand? ").lower()
        
        if action == 'hit':
            card = deal_card()
            player_cards.append(card)
            print(f"You drew: {card}")
            player_score = calculate_score(player_cards)
            print(f"Player's cards: {player_cards}")
            
            if player_score == 21:
                print("You got blackjack!")
                return
            
            if player_score > 21:
                print("You busted! Dealer wins.")
                return
        elif action == 'stand':
            dealer_score = calculate_score(dealer_cards)
            
            while dealer_score < 17:
                card = deal_card()
                dealer_cards.append(card)
                dealer_score = calculate_score(dealer_cards)
            
            print(f"Dealer's cards: {dealer_cards}")
            
            if dealer_score > 21 or player_score > dealer_score:
                print("You win!")
                return
            elif player_score < dealer_score:
                print("Dealer wins.")
                return
            else:
                print("It's a tie!")
                return
        else:
            print("Invalid action. Please choose hit or stand.")
    
    if player_score == 21:
        print("You got blackjack!")
    else:
        print("You busted! Dealer wins.")

blackjack()

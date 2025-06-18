
import random

def calculate_score(hand):
    score = sum(hand)
    
    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    
    return score

def blackjack_game():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(deck)
    
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    
    print("Player's hand:", player_hand, "Score:", player_score)
    print("Dealer's hand:", [dealer_hand[0], '?'])
    
    while player_score < 21:
        action = input("Do you want to hit or stand? (h/s): ").lower()
        
        if action == 'h':
            player_hand.append(deck.pop())
            player_score = calculate_score(player_hand)
            print("Player's hand:", player_hand, "Score:", player_score)
        elif action == 's':
            break
    
    if player_score > 21:
        print("Player busts! Dealer wins.")
        return
    
    print("Dealer's hand:", dealer_hand, "Score:", dealer_score)
    
    while dealer_score < 17:
        dealer_hand.append(deck.pop())
        dealer_score = calculate_score(dealer_hand)
        print("Dealer's hand:", dealer_hand, "Score:", dealer_score)
    
    if dealer_score > 21 or player_score > dealer_score:
        print("Player wins!")
    elif player_score < dealer_score:
        print("Dealer wins!")
    else:
        print("It's a tie!")
        
blackjack_game()


import random

def calculate_score(cards):
    score = 0
    has_ace = False
    
    for card in cards:
        if card in 'JQK':
            score += 10
        elif card == 'A':
            has_ace = True
            score += 11
        else:
            score += int(card)
    
    while score > 21 and has_ace:
        score -= 10
    
    return score

def blackjack_game():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)
    
    player_cards = [deck.pop(), deck.pop()]
    dealer_cards = [deck.pop(), deck.pop()]
    
    print('Player cards:', player_cards)
    print('Dealer card:', dealer_cards[0])
    
    while True:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        
        if player_score == 21:
            print('Player wins!')
            break
        elif player_score > 21:
            print('Player busts. Dealer wins.')
            break
        
        action = input('Do you want to hit or stand? (h/s): ')
        
        if action == 'h':
            player_cards.append(deck.pop())
            print('Player cards:', player_cards)
        else:
            while dealer_score < 17:
                dealer_cards.append(deck.pop())
                dealer_score = calculate_score(dealer_cards)
                print('Dealer cards:', dealer_cards)
            
            if dealer_score == 21:
                print('Dealer wins!')
                break
            elif dealer_score > 21:
                print('Dealer busts. Player wins!')
                break
            elif dealer_score >= player_score:
                print('Dealer wins!')
                break
            else:
                print('Player wins!')
                break

blackjack_game()

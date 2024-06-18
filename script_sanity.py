
import random

def calculate_total(cards):
    total = 0
    num_aces = 0
    
    for card in cards:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            num_aces += 1
        else:
            total += int(card)
    
    for _ in range(num_aces):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1
    
    return total

def play_game():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)
    
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)
    
    print(f"Player's hand: {player_hand}, Total: {player_total}")
    print(f"Dealer's hand: {dealer_hand[0]}, Total: {dealer_total}")
    
    while player_total < 21:
        player_action = input("Do you want to hit or stand? (h/s): ")
        
        if player_action == 'h':
            new_card = deck.pop()
            player_hand.append(new_card)
            player_total = calculate_total(player_hand)
            print(f"Player's hand: {player_hand}, Total: {player_total}")
        elif player_action == 's':
            break
    
    if player_total > 21:
        print("Player busts! Dealer wins.")
        return
    
    while dealer_total < 17:
        new_card = deck.pop()
        dealer_hand.append(new_card)
        dealer_total = calculate_total(dealer_hand)
    
    print(f"Dealer's hand: {dealer_hand}, Total: {dealer_total}")
    
    if dealer_total > 21 or player_total > dealer_total:
        print("Player wins!")
    elif player_total < dealer_total:
        print("Dealer wins.")
    else:
        print("It's a tie!")

play_game()

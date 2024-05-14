
import random

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_total(hand):
    total = sum(hand)
    if total > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        total = sum(hand)
    return total

def blackjack():
    player_hand = []
    dealer_hand = []

    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    print("Dealer's hand:", dealer_hand[0])
    print("Your hand:", player_hand)

    while calculate_total(player_hand) < 21:
        action = input("Do you want to hit or stand? (h/s): ")
        if action == 'h':
            player_hand.append(deal_card())
            print("Your hand:", player_hand)
        elif action == 's':
            break

    player_total = calculate_total(player_hand)

    if player_total > 21:
        print("Busted! You lose.")
        return

    while calculate_total(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    dealer_total = calculate_total(dealer_hand)

    print("Dealer's hand:", dealer_hand)
    print("Your total:", player_total)
    print("Dealer's total:", dealer_total)

    if dealer_total > 21 or player_total > dealer_total:
        print("You win!")
    elif player_total < dealer_total:
        print("Dealer wins.")
    else:
        print("It's a tie!")

blackjack()

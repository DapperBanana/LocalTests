
import random

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_hand(hand):
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def main():
    player_hand = []
    dealer_hand = []

    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    print("Player's hand:", player_hand)
    print("Dealer's hand:", [dealer_hand[0], '*'])

    while True:
        player_total = calculate_hand(player_hand)
        dealer_total = calculate_hand(dealer_hand)

        if player_total == 21:
            print("Player wins with a Blackjack!")
            break
        elif player_total > 21:
            print("Player busts, dealer wins!")
            break

        action = input("Do you want to hit or stand? (h/s): ")

        if action == 'h':
            player_hand.append(deal_card())
            print("Player's hand:", player_hand)
        elif action == 's':
            while dealer_total < 17:
                dealer_hand.append(deal_card())
                dealer_total = calculate_hand(dealer_hand)
            print("Player's hand:", player_hand)
            print("Player's total:", player_total)
            print("Dealer's hand:", dealer_hand)
            print("Dealer's total:", dealer_total)
            
            if dealer_total > 21 or player_total > dealer_total:
                print("Player wins!")
            elif player_total == dealer_total:
                print("It's a tie!")
            else:
                print("Dealer wins!")
            break

if __name__ == "__main__":
    main()


import random

def determine_card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card = random.choice(cards)
    return card

def calculate_hand_value(hand):
    value = sum([determine_card_value(card) for card in hand])
    num_aces = hand.count('A')

    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1

    return value

def print_hand(player, dealer, reveal_dealer_card):
    print("Your hand:", player)
    if reveal_dealer_card:
        print("Dealer's hand:", dealer)
    else:
        print("Dealer's hand:", [dealer[0], "???"])

def blackjack():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    print_hand(player_hand, dealer_hand, False)

    player_hand_value = calculate_hand_value(player_hand)
    dealer_hand_value = calculate_hand_value(dealer_hand)

    while player_hand_value < 21:
        action = input("Do you want to hit or stand? ")

        if action.lower() == 'hit':
            player_hand.append(deal_card())
            player_hand_value = calculate_hand_value(player_hand)
            print_hand(player_hand, dealer_hand, False)
        elif action.lower() == 'stand':
            break

    print_hand(player_hand, dealer_hand, True)

    while dealer_hand_value < 17:
        dealer_hand.append(deal_card())
        dealer_hand_value = calculate_hand_value(dealer_hand)

    print("Final hands:")
    print_hand(player_hand, dealer_hand, True)

    if player_hand_value > 21:
        print("You busted! Dealer wins.")
    elif dealer_hand_value > 21:
        print("Dealer busted! You win.")
    elif player_hand_value > dealer_hand_value:
        print("You win!")
    elif player_hand_value < dealer_hand_value:
        print("Dealer wins.")
    else:
        print("It's a tie!")

if __name__ == '__main__':
    blackjack()

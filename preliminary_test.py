
import random

def shuffle_deck():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        if card.isdigit():
            value += int(card)
        elif card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            num_aces += 1
            value += 11
        else:
            print("Invalid card:", card)

    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1

    return value

def print_hand(hand):
    print("Hand:", hand, "Value:", calculate_hand_value(hand))

def blackjack():
    deck = shuffle_deck()

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print_hand(player_hand)
    print("Dealer's Hand:", dealer_hand[0])

    while calculate_hand_value(player_hand) < 21:
        action = input("Do you want to hit or stand? ").lower()

        if action == 'hit':
            player_hand.append(deck.pop())
            print_hand(player_hand)
        elif action == 'stand':
            break
        else:
            print("Invalid action")

    player_score = calculate_hand_value(player_hand)

    if player_score > 21:
        print("Bust! You lose.")
    else:
        print("Dealer's Hand:")
        print_hand(dealer_hand)

        while calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
            print_hand(dealer_hand)

        dealer_score = calculate_hand_value(dealer_hand)

        if dealer_score > 21 or player_score > dealer_score:
            print("You win!")
        elif player_score < dealer_score:
            print("You lose.")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    blackjack()

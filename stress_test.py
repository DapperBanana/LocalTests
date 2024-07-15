
import random

def check_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        if card.isdigit():
            value += int(card)
        elif card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            num_aces += 1
        else:
            print("Invalid card:", card)

    for _ in range(num_aces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1

    return value

def display_hand(hand, hidden=False):
    if hidden:
        print("Hand: ", hand[0], "XX")
    else:
        print("Hand:", " ".join(hand), "Value:", check_hand_value(hand))

def blackjack_game():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    player_hand = []
    dealer_hand = []

    random.shuffle(deck)

    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    display_hand(player_hand)
    display_hand(dealer_hand, hidden=True)

    # Player's turn
    while True:
        choice = input("Do you want to hit or stand? (h/s): ")

        if choice == 'h':
            player_hand.append(deck.pop())
            display_hand(player_hand)
            if check_hand_value(player_hand) > 21:
                print("Bust! You lose.")
                return

        elif choice == 's':
            break

        else:
            print("Invalid input. Please enter 'h' or 's'.")

    # Dealer's turn
    display_hand(dealer_hand, hidden=False)

    while check_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        display_hand(dealer_hand, hidden=False)

    player_value = check_hand_value(player_hand)
    dealer_value = check_hand_value(dealer_hand)

    if player_value > 21:
        print("You bust! You lose.")
    elif dealer_value > 21:
        print("Dealer busts! You win.")
    elif player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("You lose.")
    else:
        print("It's a tie.")

blackjack_game()

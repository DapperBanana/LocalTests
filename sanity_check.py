
import random

# Function to calculate the total value of a hand
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
        else:
            print("Invalid card: " + card)
    for _ in range(num_aces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1
    return value

# Function to draw a card
def draw_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

# Main game loop
def blackjack():
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    print("Player's hand: " + ' '.join(player_hand))
    print("Dealer's hand: " + dealer_hand[0] + " ?")

    # Player's turn
    while calculate_hand_value(player_hand) < 21:
        action = input("Do you want to [H]it or [S]tand? ").upper()
        if action == 'H':
            player_hand.append(draw_card())
            print("Player's hand: " + ' '.join(player_hand))
        elif action == 'S':
            break

    player_value = calculate_hand_value(player_hand)
    if player_value > 21:
        print("Player busts! Dealer wins.")
        return

    # Dealer's turn
    print("Dealer's hand: " + ' '.join(dealer_hand))
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(draw_card())
        print("Dealer draws a card.")

    dealer_value = calculate_hand_value(dealer_hand)

    # Determine winner
    print("Player's hand value: " + str(player_value))
    print("Dealer's hand value: " + str(dealer_value))
    if dealer_value > 21 or player_value > dealer_value:
        print("Player wins!")
    elif dealer_value > player_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Start the game
blackjack()

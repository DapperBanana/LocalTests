
import random

def generate_deck():
    deck = []
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    for suit in suits:
        for face in faces:
            card = (face, suit)
            deck.append(card)

    random.shuffle(deck)
    return deck

def get_card_value(card):
    face = card[0]
    if face in ['J', 'Q', 'K']:
        return 10
    elif face == 'A':
        return 11
    else:
        return int(face)

def calculate_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        value += get_card_value(card)
        if card[0] == 'A':
            num_aces += 1

    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1

    return value

def player_turn(deck, player_hand):
    while True:
        print("Player's hand:", player_hand)
        player_value = calculate_hand_value(player_hand)
        print("Player's hand value:", player_value)

        if player_value > 21:
            print("Bust! Player loses.")
            return False

        choice = input("Hit or Stand? (H/S): ").upper()

        if choice == 'H':
            player_hand.append(deck.pop())
        elif choice == 'S':
            return True
        else:
            print("Invalid choice, please try again.")

def dealer_turn(deck, dealer_hand):
    while True:
        dealer_value = calculate_hand_value(dealer_hand)

        if dealer_value < 17:
            dealer_hand.append(deck.pop())
        else:
            break

def main():
    deck = generate_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop()]

    player_turn(deck, player_hand)

    if calculate_hand_value(player_hand) <= 21:
        dealer_turn(deck, dealer_hand)
        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)

        print("\nPlayer's hand:", player_hand)
        print("Player's hand value:", player_value)
        print("\nDealer's hand:", dealer_hand)
        print("Dealer's hand value:", dealer_value)

        if dealer_value > 21 or player_value > dealer_value:
            print("Player wins!")
        elif player_value < dealer_value:
            print("Dealer wins!")
        else:
            print("It's a tie!")

if __name__ == '__main__':
    main()

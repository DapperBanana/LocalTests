
import random

def create_deck():
    deck = []
    for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
        for value in range(2, 11):
            deck.append(str(value) + " of " + suit)
        for face_card in ["Jack", "Queen", "King", "Ace"]:
            deck.append(face_card + " of " + suit)
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        if card.split()[0] in ["Jack", "Queen", "King"]:
            value += 10
        elif card.split()[0] == "Ace":
            num_aces += 1
        else:
            value += int(card.split()[0])
    
    for _ in range(num_aces):
        if value + 11 > 21:
            value += 1
        else:
            value += 11
    return value

def display_hand(hand):
    print(", ".join(hand))
    print("Total value:", calculate_hand_value(hand))

def blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("Player's Hand:")
    display_hand(player_hand)

    print("\nDealer's Hand:")
    print(dealer_hand[0], "and one face down card")

    while True:
        if calculate_hand_value(player_hand) == 21:
            print("\nPlayer got Blackjack! Player wins!")
            break
        elif calculate_hand_value(player_hand) > 21:
            print("\nPlayer busts! Dealer wins!")
            break

        action = input("\nDo you want to hit or stand? (h/s): ").lower()
        if action == "h":
            player_hand.append(deck.pop())
            print("\nPlayer's Hand:")
            display_hand(player_hand)
        elif action == "s":
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
            print("\nPlayer's Hand:")
            display_hand(player_hand)
            print("\nDealer's Hand:")
            display_hand(dealer_hand)
            
            player_value = calculate_hand_value(player_hand)
            dealer_value = calculate_hand_value(dealer_hand)
            
            if dealer_value == 21:
                print("\nDealer got Blackjack! Dealer wins!")
            elif dealer_value > 21 or player_value > dealer_value:
                print("\nPlayer wins!")
            elif player_value < dealer_value:
                print("\nDealer wins!")
            else:
                print("\nIt's a tie!")
            break

blackjack()

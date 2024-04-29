
import random

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score -= 10 # Ace now counts as 1
    return score

def display_hand(hand):
    print("Hand: ", end="")
    for card in hand:
        print(card, end=" ")
    print()

# Initial deal
player_hand = [deal_card(), deal_card()]
dealer_hand = [deal_card()]

# Player's turn
while True:
    display_hand(player_hand)
    player_score = calculate_score(player_hand)
    print("Player Score:", player_score)

    if player_score > 21:
        print("Bust! You lose.")
        break

    choice = input("Do you want to Hit or Stand? ").lower()
    if choice == "hit":
        player_hand.append(deal_card())
    elif choice == "stand":
        break
    else:
        print("Invalid choice. Please enter Hit or Stand.")

# Dealer's turn
while calculate_score(dealer_hand) < 17:
    dealer_hand.append(deal_card())

# Display final hands
print("\nPlayer's Hand:")
display_hand(player_hand)
print("Player Score:", calculate_score(player_hand))
print("\nDealer's Hand:")
display_hand(dealer_hand)
print("Dealer Score:", calculate_score(dealer_hand))

player_score = calculate_score(player_hand)
dealer_score = calculate_score(dealer_hand)

if player_score > 21:
    print("You bust! Dealer wins.")
elif dealer_score > 21:
    print("Dealer busts! You win.")
elif player_score > dealer_score:
    print("You win!")
elif player_score < dealer_score:
    print("Dealer wins.")
else:
    print("It's a tie!")


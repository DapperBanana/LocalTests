
import random

def deal_card():
    # Generate a random number between 1 and 10 for a card value
    return random.randint(1, 10)

def calculate_score(cards):
    # Calculate the total score of the cards in hand
    score = sum(cards)
    
    # Check for blackjack (ace + 10 card) and return 0 as score
    if score == 11 and len(cards) == 2:
        return 0
    
    return score

def blackjack_game():
    player_cards = []
    dealer_cards = []
    
    # Deal two cards to the player and dealer
    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())
    
    print(f"Your cards: {player_cards}, score: {calculate_score(player_cards)}")
    print(f"Dealer's first card: {dealer_cards[0]}")
    
    # Player's turn
    while calculate_score(player_cards) < 21:
        choice = input("Do you want to hit or stand? (h/s): ")
        
        if choice == 'h':
            player_cards.append(deal_card())
            print(f"Your cards: {player_cards}, score: {calculate_score(player_cards)}")
        elif choice == 's':
            break
    
    player_score = calculate_score(player_cards)
    
    # Dealer's turn
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(deal_card())
    
    dealer_score = calculate_score(dealer_cards)
    
    # Determine the winner
    print(f"Your final score: {player_score}")
    print(f"Dealer's final score: {dealer_score}")
    
    if player_score > 21:
        print("Bust! You lose.")
    elif dealer_score > 21 or player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("Dealer wins.")
    else:
        print("It's a tie.")
    
# Play the game
while True:
    play_again = input("Do you want to play a game of blackjack? (y/n): ")
    
    if play_again.lower() != 'y':
        break
    
    blackjack_game()

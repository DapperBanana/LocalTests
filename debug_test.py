
import random

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def blackjack():
    player_cards = []
    dealer_cards = []

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    if player_score == 21:
        print("Blackjack! You win!")
        return

    while player_score < 21:
        action = input("Do you want to hit or stand? ").lower()
        if action == "hit":
            player_cards.append(deal_card())
            player_score = calculate_score(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")
        elif action == "stand":
            while dealer_score < 17:
                dealer_cards.append(deal_card())
                dealer_score = calculate_score(dealer_cards)
            print(f"Dealer's cards: {dealer_cards}, score: {dealer_score}")
            if dealer_score > 21 or player_score > dealer_score:
                print("You win!")
            elif player_score < dealer_score:
                print("Dealer wins!")
            else:
                print("It's a tie!")
            return

    print("Bust! Dealer wins!")
    return

blackjack()

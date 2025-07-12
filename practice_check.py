
import random

def deal_card():
    return random.randint(1, 10)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def blackjack():
    player_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            should_continue = input("Type 'y' to get another card, or 'n' to pass: ")

            if should_continue == 'y':
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    if player_score > 21:
        print("You went over. You lose.")
    elif computer_score > 21:
        print("Computer went over. You win!")
    elif player_score == computer_score:
        print("It's a draw.")
    elif player_score == 0:
        print("You win with a Blackjack!")
    elif computer_score == 0:
        print("Computer wins with a Blackjack!")
    elif player_score > computer_score:
        print("You win!")
    else:
        print("Computer wins.")

blackjack()

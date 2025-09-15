
import random

def draw_card():
    return random.randint(1, 10)

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        score -= 10
    return score

def blackjack():
    player_cards = [draw_card(), draw_card()]
    dealer_cards = [draw_card(), draw_card()]
    
    print("You have:", player_cards)
    print("Dealer shows:", dealer_cards[0])
    
    while True:
        choice = input("Do you want to hit or stand? (h/s): ")
        
        if choice == 'h':
            player_cards.append(draw_card())
            player_score = calculate_score(player_cards)
            print("You now have:", player_cards)
            if player_score > 21:
                print("Bust! You lose.")
                break
        elif choice == 's':
            player_score = calculate_score(player_cards)
            dealer_score = calculate_score(dealer_cards)
            print("Player score:", player_score)
            print("Dealer score:", dealer_score)
            
            while dealer_score < 17:
                dealer_cards.append(draw_card())
                dealer_score = calculate_score(dealer_cards)
            
            print("Dealer has:", dealer_cards)
            
            if dealer_score > 21:
                print("Dealer bust! You win.")
            elif player_score > dealer_score:
                print("You win!")
            elif player_score < dealer_score:
                print("Dealer wins.")
            else:
                print("It's a tie!")
            
            break
            
        else:
            print("Invalid choice. Please enter 'h' or 's'.")

blackjack()

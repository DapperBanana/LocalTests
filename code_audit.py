letion(id='chatcmpl-9TfPOceBEDusyIrzwieI5DaPyXkub', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import random

def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card = random.choice(cards)
    if card == 'A':
        return 11
    elif card in ['K', 'Q', 'J', '10']:
        return 10
    else:
        return int(card)

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

    player_turn = True
    while player_turn:
        action = input("Type 'hit' to get another card, or 'stand' to stay: ").lower()
        if action == 'hit':
            player_cards.append(deal_card())
            player_score = calculate_score(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")
            if player_score > 21:
                print("You went over 21! You lose.")
                return
        elif action == 'stand':
            player_turn = False

    while dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
        
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")

    if player_score > dealer_score or dealer_score > 21:
        print("You win!")
    elif player_score < dealer_score:
        print("You lose.")
    else:
        print("It's a tie!")

blackjack()', role='assistant', function_call=None, tool_calls=None))], created=1716857714, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=461, prompt_tokens=21, total_tokens=482)
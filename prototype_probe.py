letion(id='chatcmpl-9NQXWTlApn58N9VK6mCJSCcx3i31t', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import random

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def calculate_total(hand):
    total = 0
    num_aces = 0
    
    for card in hand:
        if card['rank'] in ['J', 'Q', 'K']:
            total += 10
        elif card['rank'] == 'A':
            num_aces += 1
        else:
            total += int(card['rank'])
    
    for i in range(num_aces):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1
    
    return total

def display_hand(hand):
    for card in hand:
        print(f"{card['rank']} of {card['suit']}")
    print(f"Total: {calculate_total(hand)}")

def play_blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    print("Player's hand:")
    display_hand(player_hand)
    print("\nDealer's hand:")
    print(f"{dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}\n")
    
    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)
    
    if player_total == 21:
        print("Blackjack! Player wins!")
        return
    
    while player_total < 21:
        action = input("Hit or Stand? (h/s): ").lower()
        
        if action == 'h':
            player_hand.append(deck.pop())
            player_total = calculate_total(player_hand)
            print("\nPlayer's hand:")
            display_hand(player_hand)
            
            if player_total == 21:
                print("21! Player wins!")
                return
            elif player_total > 21:
                print("Bust! Dealer wins.")
                return
        elif action == 's':
            break
    
    print("\nDealer's hand:")
    display_hand(dealer_hand)
    
    while dealer_total < 17:
        dealer_hand.append(deck.pop())
        dealer_total = calculate_total(dealer_hand)
    
    if dealer_total > 21:
        print("Dealer busts! Player wins!")
    elif dealer_total >= player_total:
        print("Dealer wins.")
    else:
        print("Player wins!")
    
play_blackjack()', role='assistant', function_call=None, tool_calls=None))], created=1715370590, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=571, prompt_tokens=21, total_tokens=592)
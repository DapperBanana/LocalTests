letion(id='chatcmpl-8youLSjGHT3sH9QoaUNkwl12QzZPE', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Create a deck of cards
deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

def get_card_value(card):
    if card['rank'] in ['J', 'Q', 'K']:
        return 10
    elif card['rank'] == 'A':
        return 11
    else:
        return int(card['rank'])

def calculate_total(hand):
    total = sum([get_card_value(card) for card in hand])
    num_aces = sum([1 for card in hand if card['rank'] == 'A'])
    
    while total > 21 and num_aces:
        total -= 10
        num_aces -= 1
    
    return total

def show_hand(hand, hide_first_card=False):
    if hide_first_card:
        print('Hidden card')
        for card in hand[1:]:
            print('{} of {}'.format(card['rank'], card['suit']))
    else:
        for card in hand:
            print('{} of {}'.format(card['rank'], card['suit']))

def blackjack_game():
    player_hand = [random.choice(deck), random.choice(deck)]
    dealer_hand = [random.choice(deck), random.choice(deck)]
    
    print('Player hand:')
    show_hand(player_hand)
    print('Dealer hand:')
    show_hand(dealer_hand, hide_first_card=True)
    
    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)
    
    if player_total == 21:
        print('Player has Blackjack! Player wins.')
        return
    
    while player_total < 21:
        action = input('Do you want to (h)it or (s)tand? ')
        
        if action == 'h':
            new_card = random.choice(deck)
            player_hand.append(new_card)
            player_total = calculate_total(player_hand)
            
            print('Player hand:')
            show_hand(player_hand)
            
            if player_total > 21:
                print('Player busts! Dealer wins.')
                return
        elif action == 's':
            break
    
    print('Dealer hand:')
    show_hand(dealer_hand)
    
    while dealer_total < 17:
        new_card = random.choice(deck)
        dealer_hand.append(new_card)
        dealer_total = calculate_total(dealer_hand)
        
        print('Dealer draws a card.')
    
    if dealer_total > 21:
        print('Dealer busts! Player wins.')
    elif dealer_total == player_total:
        print('It\'s a tie!')
    elif player_total > dealer_total:
        print('Player wins!')
    else:
        print('Dealer wins.')

blackjack_game()", role='assistant', function_call=None, tool_calls=None))], created=1709506061, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_2b778c6b35', usage=CompletionUsage(completion_tokens=609, prompt_tokens=21, total_tokens=630)
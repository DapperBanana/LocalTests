
import random

class Card:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f'{self.name} (Attack: {self.attack}, Defense: {self.defense})'

player_cards = [
    Card('Dragon', 10, 5),
    Card('Goblin', 4, 3),
    Card('Knight', 6, 8),
]

computer_cards = [
    Card('Elf', 5, 4),
    Card('Orc', 7, 6),
    Card('Wizard', 8, 3),
]

def play_round(player_card, computer_card):
    print(f'Player card: {player_card}')
    print(f'Computer card: {computer_card}')

    player_score = player_card.attack - computer_card.defense
    computer_score = computer_card.attack - player_card.defense

    if player_score > computer_score:
        print('Player wins!')
    elif computer_score > player_score:
        print('Computer wins!')
    else:
        print('It\'s a tie!')

# Main game loop
while True:
    player_card = random.choice(player_cards)
    computer_card = random.choice(computer_cards)

    play_round(player_card, computer_card)

    play_again = input('Do you want to play again? (y/n): ')
    if play_again.lower() != 'y':
        break

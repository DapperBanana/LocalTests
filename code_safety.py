
import random

players = []
player1 = {'name': 'Player 1', 'cards': [random.randint(1, 10) for _ in range(5)]}
player2 = {'name': 'Player 2', 'cards': [random.randint(1, 10) for _ in range(5)]}
players.append(player1)
players.append(player2)

print("Welcome to the Trading Card Game!")
print("Player 1's cards:", player1['cards'])
print("Player 2's cards:", player2['cards'])

while True:
    player1_card = random.choice(player1['cards'])
    player2_card = random.choice(player2['cards'])

    print("\nPlayer 1 plays card:", player1_card)
    print("Player 2 plays card:", player2_card)

    if player1_card > player2_card:
        print("Player 1 wins this round!")
        player1['cards'].append(player2_card)
        player2['cards'].remove(player2_card)
    elif player2_card > player1_card:
        print("Player 2 wins this round!")
        player2['cards'].append(player1_card)
        player1['cards'].remove(player1_card)
    else:
        print("It's a tie!")

    print("Player 1's cards:", player1['cards'])
    print("Player 2's cards:", player2['cards'])

    if len(player1['cards']) == 0 or len(player2['cards']) == 0:
        break

if len(player1['cards']) == 0:
    print("\nPlayer 2 wins the game!")
elif len(player2['cards']) == 0:
    print("\nPlayer 1 wins the game!")

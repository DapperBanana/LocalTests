
import random

# Define the player and opponent classes
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 20
        self.cards = []
    
    def draw_card(self):
        card = random.randint(1, 10)
        self.cards.append(card)
    
    def play_card(self):
        return self.cards.pop(0)
    
class Opponent:
    def __init__(self):
        self.health = 20
        self.cards = []
    
    def draw_card(self):
        card = random.randint(1, 10)
        self.cards.append(card)
    
    def play_card(self):
        return self.cards.pop(0)

# Initialize the player and opponent
player = Player("Player 1")
opponent = Opponent()

# Gameplay loop
while True:
    # Player's turn
    player.draw_card()
    print(f"{player.name} drew a card.")
    player_card = player.play_card()
    print(f"{player.name} played card: {player_card}")
    
    # Opponent's turn
    opponent.draw_card()
    opponent_card = opponent.play_card()
    print(f"Opponent played card: {opponent_card}")
    
    # Determine winner of the round
    if player_card > opponent_card:
        print(f"{player.name} wins the round!")
        opponent.health -= 1
    elif player_card < opponent_card:
        print("Opponent wins the round!")
        player.health -= 1
    else:
        print("It's a tie!")
    
    # Check for game over
    if player.health <= 0:
        print("Opponent wins the game!")
        break
    elif opponent.health <= 0:
        print(f"{player.name} wins the game!")
        break

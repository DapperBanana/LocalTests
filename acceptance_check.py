
import random

player_health = 20
enemy_health = 20

player_cards = []
enemy_cards = []

# Initialize player and enemy decks with random cards
for _ in range(3):
    player_cards.append(random.randint(1, 10))
    enemy_cards.append(random.randint(1, 10))

# Main game loop
while player_health > 0 and enemy_health > 0:
    print("Your health:", player_health)
    print("Enemy health:", enemy_health)
    
    # Player's turn
    print("Your cards:", player_cards)
    chosen_card = int(input("Choose a card to play: "))
    player_cards.remove(chosen_card)
    enemy_health -= chosen_card
    print("You dealt", chosen_card, "damage to the enemy.")
    
    # Enemy's turn
    chosen_card = random.choice(enemy_cards)
    enemy_cards.remove(chosen_card)
    player_health -= chosen_card
    print("Enemy dealt", chosen_card, "damage to you.")
    
# Game over
if player_health <= 0:
    print("You lose! Game over.")
elif enemy_health <= 0:
    print("You win! Congratulations.")

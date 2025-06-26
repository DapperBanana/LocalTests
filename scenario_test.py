
import random

# Define a class for the player
class Player:
    def __init__(self, name, position, skill_level):
        self.name = name
        self.position = position
        self.skill_level = skill_level

    def __str__(self):
        return f"{self.name} ({self.position}) - Skill Level: {self.skill_level}"

# Create a list of player objects
players = [
    Player("Player1", "Forward", random.randint(70, 90)),
    Player("Player2", "Midfielder", random.randint(60, 80)),
    Player("Player3", "Defender", random.randint(50, 70)),
    Player("Player4", "Goalkeeper", random.randint(40, 60))
]

# Display the list of players
print("Available Players:")
for player in players:
    print(player)

# Select players for the team
team = []
while len(team) < 11:
    player_choice = int(input("Select a player (1-4): "))
    if player_choice >= 1 and player_choice <= 4:
        if players[player_choice - 1] not in team:
            team.append(players[player_choice - 1])
        else:
            print("Player already selected. Please choose another player.")
    else:
        print("Invalid choice. Please select a player from 1-4.")

# Display the selected team
print("\nSelected Team:")
for player in team:
    print(player)


# Define a class for the players
class Player:
    def __init__(self, name, position, stats):
        self.name = name
        self.position = position
        self.stats = stats

    def display_stats(self):
        print("Name: ", self.name)
        print("Position: ", self.position)
        print("Stats: ", self.stats)

# Define a list of players
players = [
    Player("LeBron James", "Forward", {"Points": 25, "Rebounds": 10, "Assists": 5}),
    Player("Stephen Curry", "Guard", {"Points": 30, "Rebounds": 5, "Assists": 8}),
    Player("Kevin Durant", "Forward", {"Points": 27, "Rebounds": 8, "Assists": 4}),
    Player("Giannis Antetokounmpo", "Forward", {"Points": 28, "Rebounds": 12, "Assists": 6}),
    Player("James Harden", "Guard", {"Points": 32, "Rebounds": 6, "Assists": 10})
]

# Display the list of players
print("Welcome to Fantasy Sports Manager")
print("Here are the available players:")
for i, player in enumerate(players):
    print(f"{i+1}. {player.name} - {player.position}")

# Allow the user to select a player to view their stats
selection = int(input("Enter the number of the player you want to view: "))
players[selection - 1].display_stats()

# Additional features can be added such as selecting multiple players to form a team and calculating their total points
# This is a basic example to get you started

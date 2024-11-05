
class Player:
    def __init__(self, name, position, team, points):
        self.name = name
        self.position = position
        self.team = team
        self.points = points

    def __str__(self):
        return f"{self.name} - {self.position} ({self.team}) - {self.points} points"


class FantasyTeam:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_team(self):
        print(f"Fantasy Team: {self.name}")
        for player in self.players:
            print(player)

# Create some Player objects
player1 = Player("LeBron James", "SF", "Lakers", 25.3)
player2 = Player("Kevin Durant", "PF", "Nets", 28.5)
player3 = Player("Steph Curry", "PG", "Warriors", 30.1)

# Create a FantasyTeam object and add players to it
my_team = FantasyTeam("My Team")
my_team.add_player(player1)
my_team.add_player(player2)
my_team.add_player(player3)

# Display the FantasyTeam
my_team.display_team()

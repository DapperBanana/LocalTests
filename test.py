
class Player:
    def __init__(self, name, position, team):
        self.name = name
        self.position = position
        self.team = team

class FantasyTeam:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_team(self):
        print(f"Fantasy Team: {self.name}")
        print("Players:")
        for player in self.players:
            print(f"{player.name} - {player.position} - {player.team}")

# Create some players
player1 = Player("Tom Brady", "QB", "Tampa Bay Buccaneers")
player2 = Player("Derrick Henry", "RB", "Tennessee Titans")
player3 = Player("DeAndre Hopkins", "WR", "Arizona Cardinals")

# Create a fantasy team
team1 = FantasyTeam("Team 1")
team1.add_player(player1)
team1.add_player(player2)
team1.add_player(player3)

# Show the fantasy team
team1.show_team()

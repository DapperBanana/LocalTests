
class Player:
    def __init__(self, name, team, position):
        self.name = name
        self.team = team
        self.position = position
        self.points = 0

    def __str__(self):
        return f"{self.name} ({self.team} - {self.position})"

class FantasyManager:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_players(self):
        for player in self.players:
            print(player)

    def update_points(self, player_name, points):
        for player in self.players:
            if player.name == player_name:
                player.points += points

manager = FantasyManager()

player1 = Player("Tom Brady", "Tampa Bay Buccaneers", "QB")
player2 = Player("Davante Adams", "Green Bay Packers", "WR")

manager.add_player(player1)
manager.add_player(player2)

manager.update_points("Tom Brady", 20)
manager.update_points("Davante Adams", 15)

manager.display_players()

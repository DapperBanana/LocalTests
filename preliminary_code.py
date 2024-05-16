
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

    def display_team(self):
        print("Fantasy Team: " + self.name)
        for player in self.players:
            print(player.name + " - " + player.position + " - " + player.team)

def main():
    player1 = Player("LeBron James", "SF", "LAL")
    player2 = Player("Steph Curry", "PG", "GSW")
    player3 = Player("Kevin Durant", "PF", "BKN")

    team = FantasyTeam("My Team")
    team.add_player(player1)
    team.add_player(player2)
    team.add_player(player3)

    team.display_team()

if __name__ == "__main__":
    main()

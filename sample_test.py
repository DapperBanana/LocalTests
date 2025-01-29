
class Player:
    def __init__(self, name, position, points):
        self.name = name
        self.position = position
        self.points = points

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.total_points = 0

    def add_player(self, player):
        self.players.append(player)
        self.total_points += player.points

    def display_team(self):
        print(f"Team: {self.name}")
        for player in self.players:
            print(f"Player: {player.name}, Position: {player.position}, Points: {player.points}")
        print(f"Total Points: {self.total_points}")

def main():
    team_name = input("Enter your team name: ")
    team = Team(team_name)

    player1 = Player("Player1", "Forward", 10)
    player2 = Player("Player2", "Guard", 15)
    player3 = Player("Player3", "Center", 20)

    team.add_player(player1)
    team.add_player(player2)
    team.add_player(player3)

    team.display_team()

if __name__ == "__main__":
    main()

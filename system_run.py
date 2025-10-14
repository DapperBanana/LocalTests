
class Player:
    def __init__(self, name, position, points):
        self.name = name
        self.position = position
        self.points = points

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def calculate_total_points(self):
        total_points = 0
        for player in self.players:
            total_points += player.points
        return total_points

def main():
    player1 = Player("LeBron James", "SF", 35)
    player2 = Player("Steph Curry", "PG", 30)
    player3 = Player("Kevin Durant", "SF", 32)

    team = Team("My Team")
    team.add_player(player1)
    team.add_player(player2)
    team.add_player(player3)

    total_points = team.calculate_total_points()

    print(f"My {team.name} has a total of {total_points} points.")

if __name__ == "__main__":
    main()

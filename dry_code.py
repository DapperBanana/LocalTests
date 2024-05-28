
class Player:
    def __init__(self, name, position, team, points):
        self.name = name
        self.position = position
        self.team = team
        self.points = points

class FantasyTeam:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def get_total_points(self):
        total_points = 0
        for player in self.players:
            total_points += player.points
        return total_points

def main():
    team = FantasyTeam()

    print("Welcome to Fantasy Sports Manager!")
    print("Let's start by building your fantasy team.")

    while True:
        name = input("Enter player name: ")
        position = input("Enter player position: ")
        team_name = input("Enter player team: ")
        points = int(input("Enter player points: "))

        player = Player(name, position, team_name, points)
        team.add_player(player)

        another_player = input("Do you want to add another player? (yes/no): ")
        if another_player.lower() != 'yes':
            break

    print("\nYour fantasy team:")
    for player in team.players:
        print(f"{player.name} - {player.position} - {player.team} - {player.points} points")

    total_points = team.get_total_points()
    print(f"\nTotal points for your team: {total_points}")

if __name__ == "__main__":
    main()


class Player:
    def __init__(self, name, position, team):
        self.name = name
        self.position = position
        self.team = team
        self.points = 0

    def update_points(self, points):
        self.points += points

class FantasyTeam:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def get_total_points(self):
        total_points = 0
        for player in self.players:
            total_points += player.points
        return total_points

def main():
    players = [Player("Player1", "QB", "Team1"),
               Player("Player2", "RB", "Team2"),
               Player("Player3", "WR", "Team3")]

    team = FantasyTeam("MyTeam")

    print("Welcome to Fantasy Sports Manager!")

    while True:
        print("\nMenu:")
        print("1. Draft Player")
        print("2. View Team")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAvailable Players:")
            for i, player in enumerate(players):
                print(f"{i + 1}. {player.name} ({player.position} - {player.team})")

            player_choice = int(input("Enter the player number to draft: "))
            team.add_player(players[player_choice - 1])
            print(f"{players[player_choice - 1].name} has been added to your team!")

        elif choice == "2":
            print("\nYour Fantasy Team:")
            for player in team.players:
                print(f"{player.name} ({player.position} - {player.team}) - {player.points} points")
            print(f"Total Points: {team.get_total_points()}")

        elif choice == "3":
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

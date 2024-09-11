
class Player:
    def __init__(self, name, team, points):
        self.name = name
        self.team = team
        self.points = points

class FantasyTeam:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.total_points = 0

    def add_player(self, player):
        self.players.append(player)
        self.total_points += player.points

def main():
    players = [
        Player("Player 1", "Team A", 10),
        Player("Player 2", "Team B", 15),
        Player("Player 3", "Team C", 20),
        Player("Player 4", "Team D", 25),
        Player("Player 5", "Team E", 30)
    ]

    fantasy_team = FantasyTeam("My Fantasy Team")

    print("Welcome to Fantasy Ball Manager!")

    while True:
        print("\nSelect an option:")
        print("1. View Players")
        print("2. Add Player to Team")
        print("3. View Team")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nPlayers:")
            for player in players:
                print(f"{player.name} - {player.team} ({player.points} points)")

        elif choice == "2":
            print("\nChoose a player to add to your team:")
            for i, player in enumerate(players, 1):
                print(f"{i}. {player.name} - {player.team} ({player.points} points)")

            player_index = int(input("Enter player index: ")) - 1
            selected_player = players[player_index]
            fantasy_team.add_player(selected_player)
            players.remove(selected_player)
            print(f"{selected_player.name} added to your team!")

        elif choice == "3":
            print("\nFantasy Team:")
            print(f"Team Name: {fantasy_team.name}")
            print("Players:")
            for player in fantasy_team.players:
                print(f"{player.name} - {player.team} ({player.points} points)")
            print(f"Total Points: {fantasy_team.total_points}")

        elif choice == "4":
            print("Thank you for using Fantasy Ball Manager!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

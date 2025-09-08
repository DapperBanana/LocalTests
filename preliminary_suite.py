
class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class FantasyTeam:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def view_roster(self):
        print(f"Fantasy Team: {self.name}")
        print("Roster:")
        for player in self.players:
            print(f"{player.name} - {player.position}")

def main():
    print("Welcome to Fantasy Sports Manager!")

    team_name = input("Enter the name of your fantasy team: ")
    team = FantasyTeam(team_name)

    while True:
        print("\nMenu:")
        print("1. Add player")
        print("2. View roster")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            player_name = input("Enter player name: ")
            player_position = input("Enter player position: ")
            player = Player(player_name, player_position)
            team.add_player(player)
        elif choice == "2":
            team.view_roster()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

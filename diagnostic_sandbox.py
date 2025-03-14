
class Player:
    def __init__(self, name, position, team):
        self.name = name
        self.position = position
        self.team = team

    def __str__(self):
        return f"{self.name} ({self.position}) - {self.team}"

class FantasyTeam:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_team(self):
        print(f"Fantasy Team: {self.team_name}")
        print("Players:")
        for player in self.players:
            print(player)

def main():
    print("Welcome to the Fantasy Sports Manager!")
    team_name = input("Enter your fantasy team name: ")
    fantasy_team = FantasyTeam(team_name)

    while True:
        print("\nMenu:")
        print("1. Add player")
        print("2. View team")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter player name: ")
            position = input("Enter player position: ")
            team = input("Enter player team: ")
            player = Player(name, position, team)
            fantasy_team.add_player(player)
            print(f"{name} has been added to your team.")
        
        elif choice == "2":
            fantasy_team.display_team()

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

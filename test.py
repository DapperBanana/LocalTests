
class Player:
    def __init__(self, name, position, team):
        self.name = name
        self.position = position
        self.team = team

class Team:
    def __init__(self, name, players=[]):
        self.name = name
        self.players = players

    def add_player(self, player):
        self.players.append(player)

def main():
    team_name = input("Enter your team name: ")
    team = Team(team_name)

    while True:
        print("\nMenu:")
        print("1. Add player to team")
        print("2. View team roster")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            player_name = input("Enter player name: ")
            player_position = input("Enter player position: ")
            player_team = input("Enter player team: ")
            player = Player(player_name, player_position, player_team)
            team.add_player(player)
            print(f"{player_name} has been added to {team_name}'s team.")
        
        elif choice == '2':
            print(f"{team.name} Roster:")
            for player in team.players:
                print(f"{player.name} - {player.position} - {player.team}")
        
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

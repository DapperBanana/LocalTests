
class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.points = 0

class FantasyTeam:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def calculate_points(self):
        total_points = 0
        for player in self.players:
            total_points += player.points
        return total_points

def main():
    team_name = input("Enter your fantasy team name: ")
    team = FantasyTeam(team_name)

    while True:
        print("\nFantasy Sports Manager")
        print("1. Add player")
        print("2. View team points")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            player_name = input("Enter player name: ")
            player_position = input("Enter player position: ")
            new_player = Player(player_name, player_position)
            team.add_player(new_player)
        elif choice == '2':
            total_points = team.calculate_points()
            print(f"Total points for team {team.name}: {total_points}")
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            

if __name__ == "__main__":
    main()

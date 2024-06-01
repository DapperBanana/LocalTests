
class Player:
    def __init__(self, name, position, team, points):
        self.name = name
        self.position = position
        self.team = team
        self.points = points

class FantasyTeam:
    def __init__(self, name):
        self.name = name
        self.players = []
    
    def add_player(self, player):
        self.players.append(player)
    
    def display_team(self):
        print(f"Fantasy Team: {self.name}")
        total_points = 0
        for player in self.players:
            print(f"{player.name} - {player.position} - {player.team} - {player.points}")
            total_points += player.points
        print(f"Total Points: {total_points}")

def main():
    team_name = input("Enter your fantasy team name: ")
    team = FantasyTeam(team_name)
    
    while True:
        print("\nMenu:")
        print("1. Add player")
        print("2. Display team")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter player name: ")
            position = input("Enter player position: ")
            team_name = input("Enter player team: ")
            points = int(input("Enter player points: "))
            player = Player(name, position, team_name, points)
            team.add_player(player)
            print("Player added successfully.")
        elif choice == '2':
            team.display_team()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

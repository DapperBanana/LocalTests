
class FantasySportsManager:
    def __init__(self):
        self.players = []

    def add_player(self, player_name, player_position, player_team):
        self.players.append({
            'name': player_name,
            'position': player_position,
            'team': player_team
        })

    def show_players(self):
        for player in self.players:
            print(player)

# Main program
manager = FantasySportsManager()

while True:
    print("\nFantasy Sports Manager Menu:")
    print("1. Add player")
    print("2. Show players")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        player_name = input("Enter player name: ")
        player_position = input("Enter player position: ")
        player_team = input("Enter player team: ")
        manager.add_player(player_name, player_position, player_team)

    elif choice == 2:
        manager.show_players()

    elif choice == 3:
        break

    else:
        print("Invalid choice. Please try again.")

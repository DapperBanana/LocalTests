
class Player:
    def __init__(self, name, position, team):
        self.name = name
        self.position = position
        self.team = team

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

def display_players(players):
    for i, player in enumerate(players):
        print(f"{i+1}. {player.name} - {player.position} - {player.team}")

def main():
    players = [Player("LeBron James", "SF", "Lakers"),
               Player("Kevin Durant", "PF", "Nets"),
               Player("Steph Curry", "PG", "Warriors")]

    team_name = input("Enter team name: ")
    team = Team(team_name)

    while True:
        print("\nAvailable players:")
        display_players(players)
        
        choice = input("\nEnter the number of the player you want to add to your team (or 0 to exit): ")
        
        if choice == '0':
            break
        
        try:
            player_index = int(choice) - 1
            selected_player = players[player_index]
            team.add_player(selected_player)
            del players[player_index]
            print(f"{selected_player.name} added to {team.name}")
        except (IndexError, ValueError):
            print("Invalid input. Please try again.")

    print(f"\n{team.name}'s Fantasy Team:")
    display_players(team.players)

if __name__ == "__main__":
    main()


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

    def remove_player(self, player):
        self.players.remove(player)

    def display_players(self):
        print("\n" + "-"*25)
        print("Players in", self.name + "'s team:")
        for player in self.players:
            print(player.name, "-", player.position)
        print("-"*25)

def main():
    print("Welcome to Fantasy Sports Manager!")
    team_name = input("Enter your team name: ")
    team = FantasyTeam(team_name)

    print("Available positions: QB, RB, WR, TE")
    print("Enter player details or type 'exit' to quit.")

    while True:
        player_name = input("\nEnter player name: ")
        if player_name.lower() == 'exit':
            break

        player_position = input("Enter player position: ")
        player = Player(player_name, player_position)
        team.add_player(player)
        team.display_players()

    print("\nThank you for playing Fantasy Sports Manager!")


if __name__ == "__main__":
    main()

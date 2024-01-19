
import random

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.score = 0

    def update_score(self):
        self.score += random.randint(1, 10)

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def update_scores(self):
        for player in self.players:
            player.update_score()

    def get_total_score(self):
        total_score = sum([player.score for player in self.players])
        return total_score

def create_players():
    players = [
        Player("Player 1", "Forward"),
        Player("Player 2", "Forward"),
        Player("Player 3", "Midfielder"),
        Player("Player 4", "Midfielder"),
        Player("Player 5", "Defender"),
        Player("Player 6", "Defender"),
        Player("Player 7", "Goalkeeper"),
    ]
    return players

def create_teams():
    teams = [Team("Team 1"), Team("Team 2")]
    all_players = create_players()
    random.shuffle(all_players)
    for i in range(len(all_players)):
        teams[i % 2].add_player(all_players[i])
    return teams

def main():
    teams = create_teams()

    for team in teams:
        print(f"Team: {team.name}")
        for player in team.players:
            print(f"Player: {player.name} - Position: {player.position}")
        print()

    input("Press enter to start the match...")

    for _ in range(90):
        for team in teams:
            team.update_scores()

    print("Match ended!")
    for team in teams:
        print(f"Team: {team.name} - Total Score: {team.get_total_score()}")

if __name__ == "__main__":
    main()

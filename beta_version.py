
import random

class Player:
    def __init__(self, name, position, skill):
        self.name = name
        self.position = position
        self.skill = skill

    def __str__(self):
        return f"{self.name} ({self.position}) - Skill: {self.skill}"

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def print_roster(self):
        print(f"Roster for team {self.name}:")
        for player in self.players:
            print(player)

def create_team():
    team_name = input("Enter team name: ")
    team = Team(team_name)

    num_players = int(input("Enter number of players: "))
    for _ in range(num_players):
        name = input("Enter player name: ")
        position = input("Enter player position: ")
        skill = random.randint(1, 10)
        player = Player(name, position, skill)
        team.add_player(player)

    return team

def main():
    print("Welcome to Fantasy Sports Manager!")

    team1 = create_team()
    team2 = create_team()

    print("\nTeam rosters:")
    team1.print_roster()
    print()
    team2.print_roster()

if __name__ == "__main__":
    main()

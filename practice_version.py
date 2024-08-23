
import random

class Player:
    def __init__(self, name, position, skill_level):
        self.name = name
        self.position = position
        self.skill_level = skill_level

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def get_player_count(self):
        return len(self.players)

    def get_average_skill_level(self):
        total_skill_level = sum(player.skill_level for player in self.players)
        return total_skill_level / len(self.players)

def create_player(name, position):
    skill_level = random.randint(1, 10)
    return Player(name, position, skill_level)

def main():
    team_name = input("Enter your team name: ")
    team = Team(team_name)

    for _ in range(5):
        player_name = input("Enter player name: ")
        player_position = input("Enter player position: ")
        player = create_player(player_name, player_position)
        team.add_player(player)

    team_size = team.get_player_count()
    average_skill_level = team.get_average_skill_level()

    print(f"Your team {team.name} has {team_size} players.")
    print(f"The average skill level of your team is {average_skill_level:.2f}.")

if __name__ == "__main__":
    main()

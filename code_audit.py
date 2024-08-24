
import random

class Player:
    def __init__(self, name, position, skill_level):
        self.name = name
        self.position = position
        self.skill_level = skill_level
        self.points = 0

    def play_game(self):
        if self.position == "goalie":
            self.points = random.randint(0, 10)
        else:
            self.points = random.randint(0, 30) + self.skill_level

    def display_player_info(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Skill Level: {self.skill_level}")
        print(f"Points: {self.points}")


class FantasyTeam:
    def __init__(self, players):
        self.players = players

    def play_weekly_game(self):
        total_points = 0
        for player in self.players:
            player.play_game()
            total_points += player.points
        return total_points

    def display_team_info(self):
        for player in self.players:
            player.display_player_info()


def main():
    player1 = Player("John Doe", "forward", 5)
    player2 = Player("Jane Smith", "midfielder", 7)
    player3 = Player("Mike Johnson", "defender", 6)
    player4 = Player("Sarah Brown", "goalie", 8)

    team = FantasyTeam([player1, player2, player3, player4])

    team.display_team_info()

    weekly_score = team.play_weekly_game()
    print(f"Total points for the week: {weekly_score}")


if __name__ == "__main__":
    main()

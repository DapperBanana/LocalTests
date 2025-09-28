
import random

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.skill_level = random.randint(1, 10)

    def __str__(self):
        return(f"{self.name} - {self.position} (Skill Level: {self.skill_level})")

class Team:
    def __init__(self, name):
        self.name = name
        self.players = {}

    def add_player(self, player):
        self.players[player.name] = player

    def get_total_skill_level(self):
        total_skill_level = 0
        for player in self.players.values():
            total_skill_level += player.skill_level
        return total_skill_level

    def __str__(self):
        return self.name

def create_players():
    players = []
    players.append(Player("Player1", "Forward"))
    players.append(Player("Player2", "Forward"))
    players.append(Player("Player3", "Forward"))
    players.append(Player("Player4", "Midfielder"))
    players.append(Player("Player5", "Midfielder"))
    players.append(Player("Player6", "Defender"))
    players.append(Player("Player7", "Defender"))
    players.append(Player("Player8", "Goalkeeper"))
    
    return players

def create_teams():
    team1 = Team("Team1")
    team2 = Team("Team2")

    players = create_players()
    random.shuffle(players)

    for index, player in enumerate(players):
        if index % 2 == 0:
            team1.add_player(player)
        else:
            team2.add_player(player)

    return team1, team2

def main():
    team1, team2 = create_teams()

    print(f"{team1} Players:")
    for player in team1.players.values():
        print(player)

    print()

    print(f"{team2} Players:")
    for player in team2.players.values():
        print(player)

    print()

    team1_total_skill = team1.get_total_skill_level()
    team2_total_skill = team2.get_total_skill_level()

    print(f"{team1} Total Skill Level: {team1_total_skill}")
    print(f"{team2} Total Skill Level: {team2_total_skill}")

    if team1_total_skill > team2_total_skill:
        print(f"{team1} wins!")
    elif team2_total_skill > team1_total_skill:
        print(f"{team2} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()


import random

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.rating = random.randint(60, 100)

    def __str__(self):
        return f"{self.name} - {self.position} - Rating: {self.rating}"

class FantasyManager:
    def __init__(self):
        self.players = []
        self.create_players()

    def create_players(self):
        positions = ['QB', 'RB', 'WR', 'TE']
        names = ['Tom Brady', 'LeVeon Bell', 'Antonio Brown', 'Rob Gronkowski', 'Aaron Rodgers', 'Davante Adams']
        for name in names:
            position = random.choice(positions)
            player = Player(name, position)
            self.players.append(player)

    def list_players(self):
        for player in self.players:
            print(player)

    def simulate_match(self):
        team1 = random.sample(self.players, 3)
        team2 = random.sample(self.players, 3)

        team1_score = sum(player.rating for player in team1)
        team2_score = sum(player.rating for player in team2)

        print("Team 1:")
        for player in team1:
            print(player)

        print(f"Team 1 Score: {team1_score}")
        print("")

        print("Team 2:")
        for player in team2:
            print(player)

        print(f"Team 2 Score: {team2_score}")
        print("")

        if team1_score > team2_score:
            print("Team 1 wins!")
        elif team2_score > team1_score:
            print("Team 2 wins!")
        else:
            print("It's a tie!")

manager = FantasyManager()

print("Welcome to Fantasy Sports Manager!")
print("")
print("List of players:")
manager.list_players()
print("")
print("Simulating match...")
print("")
manager.simulate_match()


import random

team_a = {"player1": "Alice", "player2": "Bob", "player3": "Charlie"}
team_b = {"player1": "David", "player2": "Eve", "player3": "Frank"}

players = [team_a, team_b]

def random_score():
    return random.randint(50, 100)

def fantasy_sports_manager():
    print("Welcome to the Magic Ball League Fantasy Sports Manager!")
    print("Team A:", team_a)
    print("Team B:", team_b)

    for i in range(3):
        print("\nRound", i+1)
        for team in players:
            print("It's", team["player1"], "'s turn to play.")
            score = random_score()
            print(team["player1"], "scored", score, "points.")

            print("It's", team["player2"], "'s turn to play.")
            score = random_score()
            print(team["player2"], "scored", score, "points.")

            print("It's", team["player3"], "'s turn to play.")
            score = random_score()
            print(team["player3"], "scored", score, "points.")

    print("\nFinal Scores:")
    print("Team A:", sum([random_score() for i in range(3)]))
    print("Team B:", sum([random_score() for i in range(3)]))

fantasy_sports_manager()

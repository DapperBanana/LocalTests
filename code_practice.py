letion(id='chatcmpl-9jstkr8rsQI7P74CKulnpDTkHB36N', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import random

class Player:
    def __init__(self, name, position, skill_level):
        self.name = name
        self.position = position
        self.skill_level = skill_level

    def __str__(self):
        return f"{self.name} - {self.position} ({self.skill_level})"

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                break

    def get_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def list_players(self):
        print(f"{self.name} Players:")
        for player in self.players:
            print(player)

class FantasySportsManager:
    def __init__(self):
        self.teams = []

    def create_team(self, team_name):
        new_team = Team(team_name)
        self.teams.append(new_team)
        print(f"Team {team_name} created successfully!")

    def add_player_to_team(self, team_name, player):
        for team in self.teams:
            if team.name == team_name:
                team.add_player(player)
                print(f"Player {player.name} added to team {team_name}")
                break

    def remove_player_from_team(self, team_name, player_name):
        for team in self.teams:
            if team.name == team_name:
                team.remove_player(player_name)
                print(f"Player {player_name} removed from team {team_name}")
                break

    def list_players_on_team(self, team_name):
        for team in self.teams:
            if team.name == team_name:
                team.list_players()
                break

# Main code
manager = FantasySportsManager()

# Create teams
manager.create_team("Team A")
manager.create_team("Team B")

# Create players
player1 = Player("Player 1", "Forward", 90)
player2 = Player("Player 2", "Defense", 85)
player3 = Player("Player 3", "Goalkeeper", 95)

# Add players to teams
manager.add_player_to_team("Team A", player1)
manager.add_player_to_team("Team A", player2)
manager.add_player_to_team("Team B", player3)

# List players on teams
manager.list_players_on_team("Team A")
manager.list_players_on_team("Team B")

# Remove player from team
manager.remove_player_from_team("Team A", "Player 1")

# List players on teams after removal
manager.list_players_on_team("Team A")
manager.list_players_on_team("Team B")', role='assistant', function_call=None, tool_calls=None))], created=1720722816, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=579, prompt_tokens=21, total_tokens=600)
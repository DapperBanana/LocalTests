letion(id='chatcmpl-9JT4tnMdvXvlWNp31FX8NsouQaJUt', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import random

class Player:
    def __init__(self, name, skill_level):
        self.name = name
        self.skill_level = skill_level

class FantasyTeam:
    def __init__(self):
        self.players = []
    
    def add_player(self, player):
        self.players.append(player)
    
    def get_team_skill_level(self):
        total_skill_level = 0
        for player in self.players:
            total_skill_level += player.skill_level
        return total_skill_level

def main():
    players = [Player("Player1", 80), Player("Player2", 85), Player("Player3", 90), Player("Player4", 75), Player("Player5", 95)]
    
    my_team = FantasyTeam()
    
    while len(my_team.players) < 3:
        print("Available players:")
        for i, player in enumerate(players):
            print(f"{i+1}. {player.name} - Skill Level: {player.skill_level}")
        
        choice = int(input("Select a player to add to your team: ")) - 1
        
        if players[choice] not in my_team.players:
            my_team.add_player(players[choice])
            print(f"{players[choice].name} added to your team!")
        else:
            print("Player already in your team. Choose another player.")
    
    print("Your team is complete! Here is your team:")
    for player in my_team.players:
        print(f"{player.name} - Skill Level: {player.skill_level}")
    
    team_skill_level = my_team.get_team_skill_level()
    print(f"Total team skill level: {team_skill_level}")
    
    opponent_skill_level = random.randint(250, 350)
    print(f"Your opponent's skill level: {opponent_skill_level}")
    
    if team_skill_level > opponent_skill_level:
        print("Congratulations! You win!")
    elif team_skill_level == opponent_skill_level:
        print("It's a tie!")
    else:
        print("You lose. Better luck next time!")

if __name__ == "__main__":
    main()', role='assistant', function_call=None, tool_calls=None))], created=1714427035, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3b956da36b', usage=CompletionUsage(completion_tokens=435, prompt_tokens=21, total_tokens=456)
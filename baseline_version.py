
import random

class Player:
    def __init__(self, name, position, skill_level):
        self.name = name
        self.position = position
        self.skill_level = skill_level

    def __str__(self):
        return f"{self.name} ({self.position}) - Skill Level: {self.skill_level}"

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

    def get_best_player(self):
        best_player = max(self.players, key=lambda x: x.skill_level)
        return best_player

    def __str__(self):
        return f"{self.name} - Players: {', '.join([player.name for player in self.players])}"

def create_team():
    team_name = input("Enter team name: ")
    team = Team(team_name)
    return team

def create_player():
    name = input("Enter player name: ")
    position = input("Enter player position: ")
    skill_level = random.randint(1, 100)
    player = Player(name, position, skill_level)
    return player

def main():
    teams = []
    
    while True:
        print("\n1. Create Team")
        print("2. Add Player to Team")
        print("3. Remove Player from Team")
        print("4. View Best Player in Team")
        print("5. View Team List")
        print("6. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            team = create_team()
            teams.append(team)
            print(f"Team '{team.name}' created successfully!")
            
        elif choice == '2':
            team_name = input("Enter team name: ")
            player = create_player()
            for team in teams:
                if team.name == team_name:
                    team.add_player(player)
                    print(f"Player '{player.name}' added to team '{team_name}' successfully!")
                    break
            else:
                print(f"Team '{team_name}' not found.")
                
        elif choice == '3':
            team_name = input("Enter team name: ")
            player_name = input("Enter player name: ")
            for team in teams:
                if team.name == team_name:
                    team.remove_player(player_name)
                    print(f"Player '{player_name}' removed from team '{team_name}' successfully!")
                    break
            else:
                print(f"Team '{team_name}' not found.")
        
        elif choice == '4':
            team_name = input("Enter team name: ")
            for team in teams:
                if team.name == team_name:
                    best_player = team.get_best_player()
                    print(f"The best player in team '{team_name}' is:")
                    print(best_player)
                    break
            else:
                print(f"Team '{team_name}' not found.")
        
        elif choice == '5':
            print("Team List:")
            for team in teams:
                print(team)
        
        elif choice == '6':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

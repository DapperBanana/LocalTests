
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = random.randint(5, 20)
    
    def take_damage(self, damage):
        self.health -= damage
    
    def is_alive(self):
        return self.health > 0

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    
    current_player = player1
    
    while player1.is_alive() and player2.is_alive():
        print(f"{current_player.name}'s turn")
        print(f"{player1.name}: {player1.health} HP")
        print(f"{player2.name}: {player2.health} HP")
        
        print("Press Enter to attack!")
        input()
        
        damage = current_player.attack
        if current_player == player1:
            player2.take_damage(damage)
            print(f"{player1.name} attacks {player2.name} for {damage} damage!")
            current_player = player2
        else:
            player1.take_damage(damage)
            print(f"{player2.name} attacks {player1.name} for {damage} damage!")
            current_player = player1
        
        print()
    
    if player1.health <= 0:
        print(f"{player2.name} wins!")
    else:
        print(f"{player1.name} wins!")

if __name__ == "__main__":
    main()

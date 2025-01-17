
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        
        if board[row][col] == " ":
            board[row][col] = player
            
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            
            if all(all(cell != " " for cell in row) for row in board):
                print_board(board)
                print("It's a tie!")
                break
            
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()

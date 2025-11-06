
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(position == player for position in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter column (0-2): "))
        
        if board[row][col] != " ":
            print("Position is already taken. Try again.")
            continue
        
        board[row][col] = player
        
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        if all(all(position != " " for position in row) for row in board):
            print_board(board)
            print("It's a tie!")
            break
        
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()

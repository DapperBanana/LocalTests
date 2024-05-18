
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]
        
    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != ' ':
            return board[0][col]
        
    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != ' ':
        return board[0][0]
    
    if len(set([board[i][2-i] for i in range(3)])) == 1 and board[0][2] != ' ':
        return board[0][2]
    
    return None

def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    
    while True:
        print_board(board)
        
        row = int(input(f"Player {player}, enter row number (1-3): ")) - 1
        col = int(input(f"Player {player}, enter column number (1-3): ")) - 1
        
        if board[row][col] != ' ':
            print("That position is already taken. Try again.")
            continue
        
        board[row][col] = player
        
        winner = check_winner(board)
        
        if winner:
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    main()

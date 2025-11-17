
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != '-':
            return row[0]
    
    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != '-':
            return board[0][col]
    
    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != '-':
        return board[0][0]
    if len(set([board[i][2-i] for i in range(3)])) == 1 and board[0][2] != '-':
        return board[0][2]
    
    return None

def main():
    player = 'X'
    board = [['-' for _ in range(3)] for _ in range(3)]
    
    while True:
        print_board(board)
        row = int(input(f"Player {player}, enter row number (0-2): "))
        col = int(input(f"Player {player}, enter column number (0-2): "))
        
        if board[row][col] == '-':
            board[row][col] = player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            if all(all(cell != '-' for cell in row) for row in board):
               print_board(board)
               print("It's a tie!")
               break
            player = 'X' if player == 'O' else 'O'
        else:
            print("That spot is already taken, please choose another spot.")

if __name__ == "__main__":
    main()

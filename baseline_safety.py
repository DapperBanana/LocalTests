
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)

        player = players[current_player]
        print(f"Player {player}'s turn")

        move = input("Enter your move (e.g. 1,2): ")
        row, col = map(int, move.split(","))
        
        if board[row-1][col-1] == " ":
            board[row-1][col-1] = player

            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break

            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = (current_player + 1) % 2
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()

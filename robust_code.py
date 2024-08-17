
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board):
    # Check rows
    for row in board:
        if all(cell == row[0] for cell in row) and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == board[0][col] for row in board) and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

def tictactoe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
        col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("That space is already taken. Try again.")
            continue

        if check_win(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tictactoe()

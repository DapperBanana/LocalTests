
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    winner = None

    print_board(board)

    while winner is None:
        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter column (0-2): "))

        if board[row][col] != " ":
            print("That position is already taken. Try again.")
            continue

        board[row][col] = player
        print_board(board)

        winner = check_winner(board)
        if winner is not None:
            print(f"Player {player} wins!")
        elif all(all(cell != " " for cell in row) for row in board):
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()

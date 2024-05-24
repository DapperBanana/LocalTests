
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print_board(board)

    while True:
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter col (0, 1, or 2): "))

        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("Invalid move! Try again.")
            continue

        print_board(board)

        if check_win(board):
            print(f"Player {player} wins!")
            break

        if all(all(cell != " " for cell in row) for row in board):
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    main()

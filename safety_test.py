
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for i in range(3):
        if all([board[j][i] == player for j in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True

    return False

def tic_tac_toe():
    board = [[" ", " ", " "] for _ in range(3)]
    player = "X"

    print_board(board)

    while True:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
            board[row][col] = player
            print_board(board)

            if check_winner(board, player):
                print(f"Player {player} wins!")
                break

            player = "O" if player == "X" else "X"
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    tic_tac_toe()

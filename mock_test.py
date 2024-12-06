
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

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row = int(input("Enter row: ")) - 1
        col = int(input("Enter column: ") - 1

        if board[row][col] != " ":
            print("That space is already taken. Try again.")
            continue

        board[row][col] = player
        print_board(board)

        if check_winner(board, player):
            print(f"Player {player} wins!")
            break

        player = "X" if player == "O" else "O"

if __name__ == "__main__":
    main()

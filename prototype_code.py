
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
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
    return all(all(cell != ' ' for cell in row) for row in board)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")
        row = int(input("Enter row number (0-2): "))
        col = int(input("Enter column number (0-2): "))

        if board[row][col] == ' ':
            board[row][col] = player
            if check_win(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            if is_full(board):
                print_board(board)
                print("It's a tie!")
                break
            turn += 1
        else:
            print("That position is already taken, try again.")

if __name__ == "__main__":
    main()

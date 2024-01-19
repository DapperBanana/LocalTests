
def print_board(board):
    """Prints the tic-tac-toe board"""
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
            if j == 2:
                print("|")
        print("---------")

def check_win(board):
    """Checks if there is a winner"""
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

def check_draw(board):
    """Checks if the game is a draw"""
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def play_game():
    """Plays the tic-tac-toe game"""
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    current_player = "X"

    while True:
        print_board(board)

        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player

        if check_win(board):
            print_board(board)
            print("Player", current_player, "wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()

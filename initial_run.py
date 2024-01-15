
# Function to print the current status of the board
def print_board(board):
    print("---------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(cell + " ", end="")
        print("|")
    print("---------")

# Function to check if any player has won the game
def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

# Main game loop
def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    current_player = "X"

    while True:
        print_board(board)

        # Get player input
        row = int(input("Enter a row (0-2): "))
        col = int(input("Enter a column (0-2): "))

        # Update board with player's move
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move! Try again.")
            continue

        # Check if the game is over
        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()

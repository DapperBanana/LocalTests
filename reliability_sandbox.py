
# Function to print the tic-tac-toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check for a winning condition
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

# Function to check for a tie condition
def check_tie(board):
    return all(all(cell != " " for cell in row) for row in board)

# Initialize the board
board = [[" " for _ in range(3)] for _ in range(3)]
players = ['X', 'O']
current_player = 0

# Main game loop
while True:
    print_board(board)
    print(f"Player {players[current_player]}'s turn")
    
    # Get player input
    while True:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] == " ":
            board[row][col] = players[current_player]
            break
        else:
            print("Cell already filled, try again")

    # Check for winning condition
    if check_winner(board, players[current_player]):
        print_board(board)
        print(f"Player {players[current_player]} wins!")
        break

    # Check for tie condition
    if check_tie(board):
        print_board(board)
        print("It's a tie!")
        break

    # Switch player
    current_player = (current_player + 1) % 2

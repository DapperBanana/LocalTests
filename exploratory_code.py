
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

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print_board(board)

    while not check_winner(board, players[current_player]) and not is_full(board):
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = players[current_player]
            print_board(board)
            current_player = (current_player + 1) % 2
        else:
            print("Invalid move. Try again.")

    if check_winner(board, players[current_player]):
        print(f"Player {players[current_player]} wins!")
    else:
        print("It's a tie.")

play_game()

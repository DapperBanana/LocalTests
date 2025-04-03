
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
    players = ['X', 'O']
    player_index = 0
    current_player = players[player_index]

    print_board(board)

    while True:
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            print_board(board)
            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            player_index = (player_index + 1) % 2
            current_player = players[player_index]
        else:
            print("That spot is already taken. Try again.")

if __name__ == "__main__":
    main()

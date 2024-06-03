
board = [' ' for _ in range(9)]
player = 'X'

def print_board():
    print(f'| {board[0]} | {board[1]} | {board[2]} |')
    print('---------')
    print(f'| {board[3]} | {board[4]} | {board[5]} |')
    print('---------')
    print(f'| {board[6]} | {board[7]} | {board[8]} |')

def check_winner():
    # Check rows
    for i in range(0, 7, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return True
    return False

def is_board_full():
    return ' ' not in board

while True:
    print_board()
    position = int(input(f'Player {player}, enter a position (1-9): ')) - 1
    if board[position] == ' ':
        board[position] = player
        if check_winner():
            print_board()
            print(f'Player {player} wins!')
            break
        if is_board_full():
            print_board()
            print('It\'s a tie!')
            break
        player = 'X' if player == 'O' else 'O'
    else:
        print('That position is already taken. Try again.')

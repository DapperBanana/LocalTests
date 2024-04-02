
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    return False

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    
    print_board(board)
    
    while True:
        row = int(input('Enter the row (0-2): '))
        col = int(input('Enter the column (0-2): '))
        
        if board[row][col] == ' ':
            board[row][col] = player
            print_board(board)
            
            if check_winner(board):
                print(f'Player {player} wins!')
                break
                
            player = 'O' if player == 'X' else 'X'
        else:
            print('That position is already taken. Try again.')
    
    play_again = input('Do you want to play again? (y/n) ')
    if play_again.lower() == 'y':
        tic_tac_toe()
    else:
        print('Thanks for playing!')

tic_tac_toe()

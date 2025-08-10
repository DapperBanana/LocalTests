
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')

def check_winner(board, player):
    for i in range(3):
        if all([x == player for x in board[i]]):
            return True
        if all([x == player for x in [board[j][i] for j in range(3)]]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    curr_player =  players[0]
    print_board(board)

    for _ in range(9):
        row, col = map(int, input(f'Player {curr_player}: Enter row and column (0-2) separated by space: ').split())
        if board[row][col] != ' ':
            print('Invalid move. Try again.')
            continue
        board[row][col] = curr_player
        print_board(board)

        if check_winner(board, curr_player):
            print(f'Player {curr_player} wins!')
            break
        curr_player = players[1] if curr_player == players[0] else players[0]
    else:
        print('It\'s a tie!')

if __name__ == '__main__':
    main()

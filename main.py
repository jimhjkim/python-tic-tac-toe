import random

def display_board(board: list) -> None:
    print('\n'*100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input() -> tuple:
    marker = ''
    
    # Keep asking Player 1 to choose X or O
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
    
    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')


def place_marker(board: list, marker: str, position: int) -> None:
    board[position] = marker


def win_check(board, mark) -> bool:
    # All rows, check if they all share the same marker
    return(
        (board[7] == board[8] == board[9] == mark) or # across the top
        (board[4] ==  board[5] == board[6] == mark) or # across the middle
        (board[1] == board[2] == board[3] == mark) or # across the bottom
        # All columns, check if they all share the same marker
        (board[7] == board[4] == board[1] == mark) or # down the left
        (board[8] ==  board[5] == board[2] == mark) or # down the middle
        (board[9] == board[6] == board[3] == mark) or # across the right
        # 2 diagonals, check if they all share the same marker
        (board[7] == board[5] == board[3] == mark) or # diagonal top left to bottom right
        (board[9] == board[5] == board[1] == mark) # diagonal top right to bottom left
    )


def choose_first() -> str:
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board: list, position: int) -> bool:
    return board[position] == ' '


def full_board_check(board: list) -> bool:
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True # board is full


def player_choice(board: list) -> int:
    position = 0

    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))
    
    return position


def replay() -> bool:
    choice = input('Play again? Enter Yes or No ')
    return choice == 'Yes'


print('Welcome to Tic Tac Toe!')
while True:
    # Set up (board -> who's first -> choose markers)
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    play_game = input('Ready to play? y or n? ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    # Gameplay
    while game_on:
        # Player 1 turn
        if turn == 'Player 1': 
            # Show the board
            display_board(board)
            # Choose a position
            position = player_choice(board)
            # Place the marker on the position
            place_marker(board, player1_marker, position)
            # Check if they won
            if win_check(board, player1_marker):
                display_board(board)
                print('Player 1 has won!')
                game_on = False
            # Check if there is a tie
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Tie game!')
                    game_on = False
                else:
                    turn = 'Player 2'
            # No tie or win? Then next player's turn
        # Player 2 turn
        else:
            # Show the board
            display_board(board)
            # Choose a position
            position = player_choice(board)
            # Place the marker on the position
            place_marker(board, player2_marker, position)
            # Check if they won
            if win_check(board, player2_marker):
                display_board(board)
                print('Player 2 has won!')
                game_on = False
            # Check if there is a tie
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Tie game!')
                    game_on = False
                else:
                    turn = 'Player 1'
            # No tie or win? Then next player's turn
    if not replay():
        break
# harshit_jain
def display_board(board):
    print(board[1], "|", board[2], "|", board[3])
    print("--|---|--")
    print(board[4], "|", board[5], "|", board[6])
    print("--|---|--")
    print(board[7], "|", board[8], "|", board[9])


def player_marker():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1,Please enter the choice from X and O:").upper()
    player1 = marker
    if player1 == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, position, marker):
    test_board[position] = marker


def win_check(board, marker):
    return ((board[1] == board[2] == board[3] == marker)
            or (board[4] == board[5] == board[6] == marker)
            or (board[7] == board[8] == board[9] == marker)
            or (board[1] == board[4] == board[7] == marker)
            or (board[2] == board[5] == board[7] == marker)
            or (board[3] == board[6] == board[9] == marker)
            or (board[1] == board[5] == board[9] == marker)
            or (board[3] == board[5] == board[7] == marker))


import random


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player1'
    else:
        return "Player2"


def display_markers():
    print('PLayer1 is:'+player1_marker)
    print('Player2 is:'+player2_marker)


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position(1-9)'))
    return position


def replay():
    choice = input('Wanna play more? Yes or No:')
    return choice == 'Yes'.lower()


print("Welcome to the Tic Tac Toe Game!")
while True:

    readytoplay = input("Ready to play? Enter 'Y' or 'N':" )
    if readytoplay == 'Y'.lower():
        game_on = True
    else:
        game_on = False
    test_board = [' '] * 10
    player1_marker, player2_marker = player_marker()
    display_markers()
    turn = choose_first()
    print(turn + ' will go first.')

    while game_on:
        if turn == "Player1":
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board,position,player1_marker)
            if win_check(test_board,player1_marker):
                display_board(test_board)
                print('Player1 has won!')
                game_on = False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('Its a tie :(')
                    game_on = False
                else:
                    turn = 'Player2'
        else:
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, position, player2_marker)
            if win_check(test_board, player2_marker):
                display_board(test_board)
                print('Player2 has won!')
                game_on = False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('Its a tie :(')
                    game_on = False
                else:
                    turn = 'Player1'
    if not replay():
              break


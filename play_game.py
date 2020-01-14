import sys
from sources.play_turn import play_turn
from sources.draw_board import print_game_2D

def play_game(board):

    while True:
        user_input = []
        user_input.append(int(input())-1)
        user_input.append(int(input())-1)
        new_board, lost = play_turn(board, user_input)

        if lost:
            print('LOST FUCKER')
            sys.exit()
        board = new_board
        print_game_2D(board)
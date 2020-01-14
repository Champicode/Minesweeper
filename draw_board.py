from array import *
from random import seed
from random import randint

#Return a 2 dimension array containing the game board

class game_board:

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = []
        for i in range(0,10):
            self.board.append([0]*self.board_size)
        self.add_bombs()

    def add_bombs(self):
        seed(1)
        self.nb_bombs = int(self.board_size/2)
        for _ in range(0, self.nb_bombs):
            x = randint(0, self.board_size-1)
            y = randint(0, self.board_size-1)
            self.board[x][y] = 1

def print_game_2D(board):
    for r in board:
        for c in r:
            print(c, end=" ")
        print()
    #Here add all the graphics properties and stuff to print it nicely from a 2D array


import time
from random import seed
from random import randint, randrange
import sys

#Return a 2 dimension array containing the game board

"""
The number of mines in a board is pre-determined. 
A Beginner board has 10 mines on an 8-by-8 board
An Intermediate board has 40 mines on a 16-by-16 board
And an Expert board has 99 mines on a 16-by-30 board
"""

def HideBoard(board):
    return [[i.replace('*', '?') if i == '*' else i for i in l] for l in board]

class GameBoard:

    def __init__(self, x_size, y_size, nb_bombs):
        self.x_size = x_size
        self.y_size = y_size
        self.nb_bombs = nb_bombs

        self.CreateBoard()

    def CreateBoard(self):
        self.board = []
        for i in range(0, self.y_size):
            self.board.append(["?"]*self.x_size)
        seed(int(time.time()))
        for _ in range(0, self.nb_bombs):
            x = randint(0, self.x_size-1)
            y = randint(0, self.y_size-1)
            self.board[x][y] = '*'

    def print_game_2D(self):
        print('#'*self.x_size*3)
        for r in self.board:
            print("#   ", end=" ")
            for c in r:
                print(c, end=" ")

            print("   #", end="")
            print()
        print('#' * self.x_size*3)

    def print_hidden_game_2D(self):
        print('#'*self.x_size*3)
        for r in self.hidden_board:
            print("#   ", end=" ")
            for c in r:
                print(c, end=" ")

            print("   #", end="")
            print()
        print('#' * self.x_size*3)

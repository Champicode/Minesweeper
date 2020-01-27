import time
from random import seed, randint

def CallNN(board):
    seed(int(time.time()) - 154630)
    x = randint(0, len(board[0])-1)
    y = randint(0, len(board)-1)
    return x, y

def HideBoard(board):
    return [[i.replace('*', '?') if i == '*' else i for i in l] for l in board]
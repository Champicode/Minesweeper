import time
from random import seed
from random import randint


class InitGame:

    def __init__(self, x_size, y_size, nb_bombs):

        self.x_size = x_size
        self.y_size = y_size
        self.nb_bombs = nb_bombs

        self.InitGameBoard()
        self.InitGrid()

    def InitGameBoard(self):
        """
        Initialize the game board that will look like
        """
        self.GameBoard = []
        for i in range(0, self.y_size):
            self.GameBoard.append(["?"]*self.x_size)
        seed(int(time.time()))
        for i in range(0, self.nb_bombs):
            x = randint(0, self.x_size-1)
            y = randint(0, self.y_size-1)
            while self.GameBoard[x][y] == '*':
                x = randint(0, self.x_size - 1)
                y = randint(0, self.y_size - 1)
            self.GameBoard[x][y] = '*'

    def InitGrid(self):
        self.Grid = []
        for i in range(0, self.x_size):
            for j in range(0, self.y_size):
                self.Grid.append([i, j])

    def UpdateBoard(self, x, y):

        if x < 0 or x > self.x_size or y < 0 or y > self.y_size:
            return False

        if self.GameBoard[x][y] == "*":
            return True

        if self.GameBoard[x][y] != "?":
            return False

        bomb_around = self.CheckBomb(x, y)
        self.GameBoard[x][y] = bomb_around

        if bomb_around == 0:
            X, Y = self.CheckBorder(x, y)
            for i in X:
                for j in Y:
                    self.UpdateBoard(i, j)

        return False

    def Flag(self, x, y):

        #If there was a flag, removes it
        if self.GameBoard[x][y] == "§":
            self.GameBoard[x][y] = "?"
            return True

        #If it was an empty cell, add a simple flag
        if self.GameBoard[x][y] == "?":
            self.GameBoard[x][y] = "§"
            return True

        #If there is a bomb, add a bomb_flag
        if self.GameBoard[x][y] == "*":
            self.GameBoard[x][y] = "*§*"
            return True

        #If there was a bomb_flag, removes it and adds back the bomb
        if self.GameBoard[x][y] == "*§*":
            self.GameBoard[x][y] = "*"
            return True

        return True

    def CheckBomb(self, x, y):
        X, Y = self.CheckBorder(x, y)
        bomb_around = 0
        for i in X:
            for j in Y:
                bomb_around += 1 if (self.GameBoard[i][j] == "*" or self.GameBoard[i][j] == "*§*") else 0
        self.GameBoard[x][y] = bomb_around
        return bomb_around

    def CheckBorder(self, x, y):
        X = [x-1, x, x+1]
        Y = [y-1, y, y+1]
        X = X[1:] if x == 0 else X             #Top border
        X = X[:-1] if x == self.x_size-1 else X   #Bottom border
        Y = Y[1:] if y == 0 else Y             #Left border
        Y = Y[:-1] if y == self.y_size-1 else Y   #Right border

        return X, Y

    def PrintGameBoard(self):
        print('#'*self.x_size*3)
        for r in self.GameBoard:
            print("#   ", end=" ")
            for c in r:
                print(c, end=" ")
            print("   #", end="")
            print()
        print('#' * self.x_size*3)

    def PrintGrid(self):
        print('#'*self.x_size*3)
        for r in self.Grid:
            print("#   ", end=" ")
            for c in r:
                print(c, end=" ")
            print("   #", end="")
            print()
        print('#' * self.x_size*3)

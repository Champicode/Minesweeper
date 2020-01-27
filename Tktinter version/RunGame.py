from DrawBoard import GameBoard
from PIL import Image, ImageTk


class PlayGameInput(GameBoard):

    def __init__(self, x_size, y_size, nb_bombs):
        GameBoard.__init__(self, x_size, y_size, nb_bombs)
        self.move_left = x_size*y_size - nb_bombs
        self.print_game_2D()
        self.start()

    def start(self):
        while True:
            self.play_turn()
            self.print_game_2D()
            if self.move_left == 0:
                self.print_win()
                return False

    def play_turn(self):

        x = int(input())-1
        y = int(input())-1

        while x < 0 or x > self.x_size-1 or y < 0 or y > self.y_size-1:
            print("again")
            x = int(input()) - 1
            y = int(input()) - 1

        self.update_board(x, y)

    def add_flag(self, x, y):
        self.board[x][y] = "§"

    def update_board(self, x, y):

        if x < 0 or x > self.x_size-1 or y < 0 or y > self.y_size-1:
            return False

        if self.board[x][y] == "*":
            self.print_lost()

        if self.board[x][y] != "?":
            return False

        bomb_around = self.check_bomb(x, y)
        self.board[x][y] = bomb_around

        if bomb_around == 0:
            X, Y = self.check_border(x, y)
            for i in X:
                for j in Y:
                    self.update_board(i, j)

        return False

    def check_bomb(self, x, y):
        X, Y = self.check_border(x, y)
        bomb_around = 0
        for i in X:
            for j in Y:
                bomb_around += 1 if self.board[i][j] == "*" else 0
        self.board[x][y] = bomb_around
        self.move_left -= 1
        return bomb_around

    def check_border(self, x, y):
        X = [x-1, x, x+1]
        Y = [y-1, y, y+1]
        X = X[1:]  if x == 0 else X             #Top border
        X = X[:-1] if x == self.x_size-1 else X   #Bottom border
        Y = Y[1:]  if y == 0 else Y             #Left border
        Y = Y[:-1] if y == self.y_size-1 else Y   #Right border

        return X, Y

class PlayGameGraphic(GameBoard):

    def __init__(self, x_size, y_size, nb_bombs):
        GameBoard.__init__(self, x_size, y_size, nb_bombs)
        self.move_left = x_size*y_size - nb_bombs

    def UpdateBoard(self, x, y):

        if x < 0 or x > self.x_size or y < 0 or y > self.y_size:
            return False

        if self.board[x][y] == "*":
            self.PrintLost()
            return True

        if self.board[x][y] != "?":
            return False

        bomb_around = self.CheckBomb(x, y)
        self.board[x][y] = bomb_around

        if bomb_around == 0:
            X, Y = self.CheckBorder(x, y)
            for i in X:
                for j in Y:
                    self.UpdateBoard(i, j)

        return False

    def flag(self, x, y):

        #If there was a flag, removes it
        if self.board[x][y] == "§":
            self.board[x][y] = "?"
            return True

        #If it was an empty cell, add a simple flag
        if self.board[x][y] == "?":
            self.board[x][y] = "§"
            return True

        #If there is a bomb, add a bomb_flag
        if self.board[x][y] == "*":
            self.board[x][y] = "*§*"
            return True

        #If there was a bomb_flag, removes it and adds back the bomb
        if self.board[x][y] == "*§*":
            self.board[x][y] = "*"
            return True

        return True

    def CheckBomb(self, x, y):
        X, Y = self.CheckBorder(x, y)
        bomb_around = 0
        for i in X:
            for j in Y:
                bomb_around += 1 if (self.board[i][j] == "*" or self.board[i][j] == "*§*") else 0
        self.board[x][y] = bomb_around
        self.move_left -= 1
        return bomb_around

    def CheckBorder(self, x, y):
        X = [x-1, x, x+1]
        Y = [y-1, y, y+1]
        X = X[1:] if x == 0 else X             #Top border
        X = X[:-1] if x == self.x_size-1 else X   #Bottom border
        Y = Y[1:] if y == 0 else Y             #Left border
        Y = Y[:-1] if y == self.y_size-1 else Y   #Right border

        return X, Y

    def PrintLost(self):
        print('Lost')

    def PrintWin(self):
        print('Win')

#play_game(x_size=8, y_size=8, nb_bombs=10)
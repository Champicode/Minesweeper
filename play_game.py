import sys
from sources.play_turn import play_turn
from sources.draw_board import game_board

class play_game(game_board):

    def __init__(self, x_size, y_size, nb_bombs):
        game_board.__init__(self, x_size, y_size, nb_bombs)
        self.start()

    def start(self):
        while True:
            self.print_game_2D()
            self.play_turn()
            #self.board = new_board

    def play_turn(self):

        x = int(input())-1
        y = int(input())-1

        while x < 0 or x > self.x_size-1 or y < 0 or y > self.y_size-1:
            print("again")
            x = int(input()) - 1
            y = int(input()) - 1

        self.update_board(x, y)

    def update_board(self, x, y):

        if x < 0 or x > self.x_size-1 or y < 0 or y > self.y_size-1:
            return False

        if self.board[x][y] != "?":
            return False

        if self.board[x][y] == "*":
            print("Lost")
            return True

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
        return bomb_around

    def check_border(self, x, y):
        X = [x-1, x, x+1]
        Y = [y-1, y, y+1]
        X = X[1:]  if x == 0 else X             #Top border
        X = X[:-1] if x == self.x_size-1 else X   #Bottom border
        Y = Y[1:]  if y == 0 else Y             #Left border
        Y = Y[:-1] if y == self.y_size-1 else Y   #Right border

        return X, Y


play_game(x_size=10, y_size=10, nb_bombs=5)
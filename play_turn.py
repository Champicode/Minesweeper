import traceback

def update_cell(game, x, y):

    #If nothing around, put 0 and propagate

    #Need to handle borders
    X = [x, x+1, x+2]
    Y = [y, y+1, y+2]

    if x == 1:#Top border
        X = X[1:]

    if x == game.x_size: #Bottom border
        X = X[:-1]

    if y == 1: #Left border
        Y = Y[1:]

    if y == game.y_size: #Right border
        Y = Y[:-1]

    bomb_around = 0
    for i in X:
        for j in Y:
            bomb_around += 1 if game.board[i][j] == "*" else 0
    game.board[x][y] = bomb_around

    if bomb_around == 0:
        for i in X:
            for j in Y:
                print_game_2D(game.board)
                update_cell(game, i, j)

    return game.board

def play_turn(game):
    try:
        x = int(input())-1
        y = int(input())-1

        cell_target = game.board[x][y]

        #Hits a bomb!
        if cell_target == "*":
            return game.board, True, True

        #Hits an already discovered cell
        if cell_target == 2:
            print_game_2D(game.board)
            return game.board, False, False


    except:
        traceback.print_exc()
        print_game_2D(game.board)
        return game.board, False, False

    print_game_2D(update_cell(game, x, y))

    return game.board, False, True

def play_turn(board, user_input):
    lost = False
    target = board[user_input[0]][user_input[1]]

    if target == 1:
        lost = True

    board[user_input[0]][user_input[1]] = 2
    return board, lost

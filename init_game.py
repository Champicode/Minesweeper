from sources.draw_board import game_board
from sources.draw_board import print_game_2D
from sources.play_game import play_game

#Initialize the board and add the bombs
game = game_board(board_size=10)

print_game_2D(game.board)

play_game(game.board)


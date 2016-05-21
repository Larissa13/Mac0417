from .chess import *
import numpy as np
from vpi.io import read_gray_image, display_image

def analyze_chess_game(image_directory):
    game = Game()
    plays = []
    board = Chessboard()
    board.print_board()
    for i in range(28):
        image = str(image_directory) + "/" + str (i) + ".png"
        f = read_gray_image(image)
        plays.append(f)
    
    n = len(plays)
    for i in range(n-1):
        diff = plays[i+1] - plays[i]
        moved = np.nonzero(diff)
        xmin, ymin = (moved[0].min(0)/60).astype(int), (moved[1].min(0)/60).astype(int)
        xmax, ymax = (moved[0].max(0)/60).astype(int), (moved[1].max(0)/60).astype(int)
        fromx, fromy, tox, toy = 0, 0, 0, 0
        if i%2 == 1:
            fromx, fromy = xmin, ymin
            tox, toy = xmax, ymax
        else:
            fromx, fromy = xmax, ymax
            tox, toy = xmin, ymin
        piece = str(board.board[fromx][fromy].piece_name)        
        print(piece, "from", (fromx, fromy), "to", (tox, toy) )
        board.set_piece(piece, tox, toy)
        board.set_piece("", fromx, fromy)
        
    return game

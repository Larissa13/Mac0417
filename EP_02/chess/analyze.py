from .chess import *
import numpy as np
from vpi.io import read_gray_image, display_image

def analyze_chess_game(image_directory):
    game = Game()
    plays = []
    board = Chessboard()
    Images = []
    for i in range(28):
        image = str(image_directory) + "/" + str (i) + ".png"
        Images.append(image)
        f = read_gray_image(image)
        plays.append(f)
    
    n = len(plays)
    for i in range(n-1):
        diff = plays[i+1] - plays[i]
        moved = np.nonzero(diff)
        xmin = (moved[0].min(0)/60).astype(int)
        xmax = (moved[0].max(0)/60).astype(int)
        y0 = np.nonzero(diff[xmin*60:(xmin+1)*60, :])
        y1 = np.nonzero(diff[(xmax)*60:(xmax+1)*60, :])
        ymin = (y0[1].min()/60).astype(int)
        ymax = (y1[1].max()/60).astype(int)
        fromx, fromy = 0, 0
        tox, toy = 0,0
        white = str(board.board[xmin][ymin].piece_name)
        black = str(board.board[xmax][ymax].piece_name)
        if (i%2==1 and (not (white == ""))) or (black == ""):
            print(str(board.board[xmin][ymin].piece_name))
            fromx, fromy = xmin, ymin
            tox, toy = xmax, ymax
        else:
            print(str(board.board[xmax][ymax].piece_name))
            fromx, fromy = xmax, ymax
            tox, toy = xmin, ymin
        
        piece0 = str(board.board[fromx][fromy].piece_name)
        piece1= str(board.board[tox][toy].piece_name)
        piece_start = ChessSquare(piece0, fromx, fromy)
        piece_stop = ChessSquare(piece1, tox, toy)
        move = Move(Images[i+1], piece_start, piece_stop)
        game.add_move(move)
        board.set_piece(piece0, tox, toy)
        board.set_piece("", fromx, fromy)


    return game
    

from .chess import *
import numpy as np
from vpi.io import read_gray_image, display_image

def analyze_chess_game(image_directory):
    game = Game()
    boards = []
    for i in range(28):
        image = str(image_directory) + "/" + str (i) + ".png"
        f = read_gray_image(image)
        boards.append(f)
    
    n = len(boards)
    for i in range(n-1):
        diff = boards[i+1] - boards[i]
        
    return game

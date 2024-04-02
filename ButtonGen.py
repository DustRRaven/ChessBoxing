from CommonValues import *
from GetChessNotation import get_chess_notation
from Classes import *
import pygame

def ButtonGen():
    cpt_button = -1
    for i in range(8):
        coordy = HEIGHT - i * SQUARE_SIZE - SQUARE_SIZE//2

        for j in range(8):
            cpt_button += 1
            coordx = j*SQUARE_SIZE + SQUARE_SIZE//2
            nom_button = f'button{get_chess_notation(cpt_button)}' ; globals()[nom_button] = Button(coordx,coordy)
            liste_buttons.append(globals()[nom_button])
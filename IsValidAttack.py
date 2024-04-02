from CommonValues import *
import IsValidMove

def test(button_clicked = tuple, prev_pos = tuple, piece = object):
    piece_type = (type(piece).__name__)

    prev_piece = chessboard[button_clicked]
    chessboard[button_clicked] = None

    if piece_type != 'Pion':
        if IsValidMove.test(button_clicked, prev_pos, piece) == True:
            return True
        else:
            chessboard[button_clicked] = prev_piece
    else:
        if IsValidMove.test(button_clicked, prev_pos, piece) == 1:
            return True
        else: chessboard[button_clicked] = prev_piece
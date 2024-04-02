from CommonValues import *
import IsValidMove

def get_roi_position(color):
    for piece in chessboard.values():
        if piece and type(piece).__name__ == 'Roi' and piece.color == color:
            case = list(chessboard.keys())[list(chessboard.values()).index(piece)]
            return case

def is_check(color):
    roi_pos =  get_roi_position(color)
    for piece in chessboard.values():
        if piece and piece.color != color:
            if IsValidMove.test(piece, roi_pos, piece):
                return True
    return False
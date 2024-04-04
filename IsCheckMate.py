from CommonValues import *
import IsValidMove
import IsValidAttack

def get_roi_position(color):
    for piece in chessboard.values():
        if piece and type(piece).__name__ == 'Roi' and piece.color == color:
            case = list(chessboard.keys())[list(chessboard.values()).index(piece)]
            return case

def is_check(color):
    global W_checkmate_cpt ; global B_checkmate_cpt
    roi_pos =  get_roi_position(color)
    for piece in chessboard.values():
        if piece and piece.color != color:
            if IsValidMove.test(roi_pos, list(chessboard.keys())[list(chessboard.values()).index(piece)], piece):
                if color==W:
                    W_checkmate_cpt += 1
                else : B_checkmate_cpt += 1
                return True
            if IsValidAttack.test(roi_pos, list(chessboard.keys())[list(chessboard.values()).index(piece)], piece):
                if color==W:
                    W_checkmate_cpt += 1
                else : B_checkmate_cpt += 1
                return True

    if color==W:
        W_checkmate_cpt = 0
    else : B_checkmate_cpt = 0
    return False

def is_checkmate(color):
    roi_pos = get_roi_position(color)
    roi_pos_list = liste_buttons.index(roi_pos)
    roi = chessboard[roi_pos]
    if is_check(color) == True:
        for move in range(3):
            if IsValidMove.test(liste_buttons[(roi_pos_list+1-move-BOARD_L)], roi_pos, roi) or IsValidAttack.test(liste_buttons[(roi_pos_list+1-move-BOARD_L)], roi_pos, roi):
                return False
            elif IsValidMove.test(liste_buttons[(roi_pos_list+1-move)], roi_pos, roi) or IsValidAttack.test(liste_buttons[(roi_pos_list+1-move)], roi_pos, roi):
                return False
            elif IsValidMove.test(liste_buttons[(roi_pos_list+1-move+BOARD_L)], roi_pos, roi) or IsValidAttack.test(liste_buttons[(roi_pos_list+1-move+BOARD_L)], roi_pos, roi):
                return False
        return True
    elif W_checkmate_cpt > 1:
        return True
    elif B_checkmate_cpt > 1:
        return True
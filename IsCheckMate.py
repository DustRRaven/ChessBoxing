from CommonValues import *
import IsValidMove
import IsValidAttack

def get_roi_position(color):
    for piece in chessboard.values():
        if piece and type(piece).__name__ == 'Roi' and piece.color == color:
            case = list(chessboard.keys())[list(chessboard.values()).index(piece)]
            return case, piece


def get_possible_moves(color):
        case_roi, roi_piece = get_roi_position(color)
        roi_pos = roi_piece.rect.center
        possible_moves = []
        start_roi_x = roi_pos[0] // SQUARE_SIZE
        start_roi_y = roi_pos[1] // SQUARE_SIZE

        for dx in [-1, 0, 1]:
            for dy in [-8, 0, 8]:
                indice_case = liste_buttons.index(case_roi)+dx+dy

                if indice_case>=0:
                    case_test = liste_buttons[indice_case]

                    new_chessboard = chessboard.copy()
                    new_chessboard[case_test] = roi_piece
                    new_chessboard[case_roi] = None
                    if dx == 0 and dy == 0:
                        continue  # Skip the position of the king itself
                    if chessboard[case_test] == None:
                        
                        if not is_check(color, new_chessboard):
                            possible_moves.append(case_test)
                    elif chessboard[case_test] != None and chessboard[case_test].color !=roi_piece.color and IsValidAttack.test(case_test, case_roi, roi_piece):
                        if not is_check(color, new_chessboard):
                            possible_moves.append(case_test)

                

        return possible_moves


def is_check(color, chessboard):
    roi_pos =  get_roi_position(color)[0]
    for danger_piece in chessboard.values():
        if danger_piece and danger_piece.color != color:
            if IsValidMove.test(roi_pos, list(chessboard.keys())[list(chessboard.values()).index(danger_piece)], danger_piece):
                return True, danger_piece
            if IsValidAttack.test(roi_pos, list(chessboard.keys())[list(chessboard.values()).index(danger_piece)], danger_piece):
                return True
    return False

def is_checkmate(color):
    
    roi_piece = get_roi_position(color)[1]
    roi_pos = get_roi_position(color)[0]
    roi_pos_list = liste_buttons.index(roi_pos)
    roi = chessboard[roi_pos]

    if not is_check(color, chessboard):
        return False
    
    possible_moves = get_possible_moves(color)

    if possible_moves:
        return False
    

    for piece in chessboard.values():
        if piece and piece.color == color:
            case_piece = list(chessboard.keys())[list(chessboard.values()).index(piece)]
            for possible_move in chessboard.keys():
                if chessboard[possible_move] is None:
                    if IsValidMove.test(possible_move, case_piece, piece):
                        print('valid move')
                        new_chessboard = chessboard.copy()
                        if new_chessboard == chessboard: print('copie réussie')
                        new_chessboard[possible_move] = piece
                        new_chessboard[case_piece] = None
                        if not is_check(color,new_chessboard):
                            print('valid block')
                            return False
                elif not chessboard[possible_move]:
                    print(chessboard[possible_move])
                    if IsValidAttack.test(possible_move, case_piece, piece):
                        new_chessboard = chessboard.copy()
                        new_chessboard[possible_move] = piece
                        new_chessboard[case_piece] = None
                        if not is_check(color,new_chessboard):
                            return False

    return True

    
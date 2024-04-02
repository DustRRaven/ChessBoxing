from CommonValues import *
def test(button_clicked = tuple, prev_pos = tuple, piece = object):
    
    team = piece.color
    operation_symbols = {'W':'+','B':'-'}
    op = operation_symbols.get(team)
    button_clicked_ob = button_clicked
    prev_pos_ob = prev_pos
    button_clicked = button_clicked.rect.center
    prev_pos = prev_pos.rect.center

    piece_type = (type(piece).__name__)

    if piece_type=='Pion':
        start_pion_x = prev_pos[0] // SQUARE_SIZE
        start_pion_y = prev_pos[1] // SQUARE_SIZE
        # 0 à 7 de gauche à droite
        end_pion_x   = button_clicked[0] // SQUARE_SIZE
        # 0 à 7 de haut en bas
        end_pion_y   =  button_clicked[1] // SQUARE_SIZE
        dist_pion_x  = end_pion_x - start_pion_x
        dist_pion_y  = end_pion_y - start_pion_y
        
        if (prev_pos[1] == liste_buttons[8].rect.center[1] and team == W):
            if abs(dist_pion_y) <= 2 and abs(dist_pion_x) == 0 and chessboard[button_clicked_ob] is None:
                return True
            
        elif prev_pos[1] == liste_buttons[55].rect.center[1] and team == B and chessboard[button_clicked_ob] is None:
            if abs(dist_pion_y) <= 2 and abs(dist_pion_x) == 0:
                return True

        elif dist_pion_y == 1 and dist_pion_x == 0 and team == B:
            return True
        elif dist_pion_y == -1 and dist_pion_x == 0 and team == W:
            return True
        elif dist_pion_y == 1 and abs(dist_pion_x) == 1 and team == B:
            return 1
        elif dist_pion_y == -1 and abs(dist_pion_x) == 1 and team ==  W:
            return 1
    

    if piece_type == 'Tour':

        start_tour_x = prev_pos[0] // SQUARE_SIZE
        start_tour_y = prev_pos[1] // SQUARE_SIZE
        # 0 à 7 de gauche à droite
        end_tour_x   = button_clicked[0] // SQUARE_SIZE
        # 0 à 7 de haut en bas
        end_tour_y   =  button_clicked[1] // SQUARE_SIZE
        dist_tour_x  = end_tour_x - start_tour_x
        dist_tour_y  = end_tour_y - start_tour_y

        # Droite
        if dist_tour_x > 0 and button_clicked[1] == prev_pos[1]:
            for tour_step in range(1, abs(dist_tour_x), 1):
                case_index = liste_buttons.index(prev_pos_ob) + tour_step
                case = liste_buttons[case_index]
                if chessboard[case] is not None:
                    return False
            return True
        
        # Gauche
        elif dist_tour_x < 0 and button_clicked[1] == prev_pos[1]:
            for tour_step in range (1, abs(dist_tour_x), 1):
                case_index = liste_buttons.index(prev_pos_ob) - tour_step
                case = liste_buttons[case_index]
                if chessboard[case] is not None:
                    return False
            return True
              
        # Haut
        elif dist_tour_y < 0 and button_clicked[0] == prev_pos[0]:
            for tour_step in range (1, abs(dist_tour_y), 1):
                case_index = liste_buttons.index(prev_pos_ob) + tour_step * BOARD_L
                case = liste_buttons[case_index]
                if chessboard[case] is not None:
                    return False
            return True
        
        # Bas
        elif dist_tour_y > 0 and button_clicked[0] == prev_pos[0]:
            for tour_step in range (1, abs(dist_tour_y), 1):
                case_index = liste_buttons.index(prev_pos_ob) - tour_step * BOARD_L
                case = liste_buttons[case_index]
                if chessboard[case] is not None:
                    return False
            return True
    
    if piece_type == 'Cavalier':
        
        if (
            button_clicked[0]//SQUARE_SIZE == (prev_pos[0]//SQUARE_SIZE) + eval(f'{op}+1')
            and button_clicked[1]//SQUARE_SIZE == (prev_pos[1]//SQUARE_SIZE)+ eval(f'{op}-2')
            ):
            return True
            
        elif (
            button_clicked[0]//SQUARE_SIZE == (prev_pos[0]//SQUARE_SIZE)+ eval(f'{op}-1')
            and button_clicked[1]//SQUARE_SIZE == (prev_pos[1]//SQUARE_SIZE)+ eval(f'{op}-2')
            ):
            return True
        elif (
            button_clicked[0]//SQUARE_SIZE == (prev_pos[0]//SQUARE_SIZE)+ eval(f'{op}-1')
            and button_clicked[1]//SQUARE_SIZE == (prev_pos[1]//SQUARE_SIZE)+ eval(f'{op}+2')
            ):
            return True
        elif (
            button_clicked[0]//SQUARE_SIZE == (prev_pos[0]//SQUARE_SIZE)+ eval(f'{op}+1')
            and button_clicked[1]//SQUARE_SIZE == (prev_pos[1]//SQUARE_SIZE)+ eval(f'{op}+2')
            ):
            return True
        elif (
            button_clicked[0]//SQUARE_SIZE == (prev_pos[0]//SQUARE_SIZE)+ eval(f'{op}+2')
            and button_clicked[1]//SQUARE_SIZE == (prev_pos[1]//SQUARE_SIZE)+ eval(f'{op}-1')
            ):
            return True
        elif (
            button_clicked[0]//SQUARE_SIZE == (prev_pos[0]//SQUARE_SIZE)+ eval(f'{op}-2')
            and button_clicked[1]//SQUARE_SIZE == (prev_pos[1]//SQUARE_SIZE)+ eval(f'{op}-1')
            ):
            return True
        elif (
            button_clicked[0]//SQUARE_SIZE == (prev_pos[0]//SQUARE_SIZE)+ eval(f'{op}+2')
            and button_clicked[1]//SQUARE_SIZE == (prev_pos[1]//SQUARE_SIZE)+ eval(f'{op}+1')
            ):
            return True
        elif (
            button_clicked[0]//SQUARE_SIZE == (prev_pos[0]//SQUARE_SIZE)+ eval(f'{op}-2')
            and button_clicked[1]//SQUARE_SIZE == (prev_pos[1]//SQUARE_SIZE)+ eval(f'{op}+1')
            ):
            return True
    
    if piece_type == 'Fou':
        start_fou_x = prev_pos[0] // SQUARE_SIZE
        start_fou_y = prev_pos[1] // SQUARE_SIZE
        # 0 à 7 de gauche à droite
        end_fou_x   = button_clicked[0] // SQUARE_SIZE
        # 0 à 7 de haut en bas
        end_fou_y   =  button_clicked[1] // SQUARE_SIZE
        dist_fou_x  = end_fou_x - start_fou_x
        dist_fou_y  = end_fou_y - start_fou_y
        
        if abs(dist_fou_x) == abs(dist_fou_y):
            # Haut droite
            if dist_fou_x > 0 and dist_fou_y < 0:
                for fou_step in range(1, abs(dist_fou_x),1):
                    case_index = liste_buttons.index(prev_pos_ob) + fou_step + fou_step*BOARD_L
                    case = liste_buttons[case_index]
                    if chessboard[case] is not None:
                        return False
                return True
            # Haut gauche
            elif dist_fou_x < 0 and dist_fou_y < 0:
                for fou_step in range(1, abs(dist_fou_x),1):
                    case_index = liste_buttons.index(prev_pos_ob) - fou_step + fou_step*BOARD_L
                    case = liste_buttons[case_index]
                    if chessboard[case] is not None:
                        return False
                return True
            # Bas droite
            elif dist_fou_x > 0 and dist_fou_y > 0:
                for fou_step in range(1, abs(dist_fou_x),1):
                    case_index = liste_buttons.index(prev_pos_ob) + fou_step - fou_step*BOARD_L
                    case = liste_buttons[case_index]
                    if chessboard[case] is not None:
                        return False
                return True
            # Bas gauche
            elif dist_fou_x < 0 and dist_fou_y > 0:
                for fou_step in range(1, abs(dist_fou_x),1):
                    case_index = liste_buttons.index(prev_pos_ob) - fou_step - fou_step*BOARD_L
                    case = liste_buttons[case_index]
                    if chessboard[case] is not None:
                        return False
                return True
            
    if piece_type == 'Reine':
        start_reine_x = prev_pos[0] // SQUARE_SIZE
        start_reine_y = prev_pos[1] // SQUARE_SIZE
        # 0 à 7 de gauche à droite
        end_reine_x   = button_clicked[0] // SQUARE_SIZE
        # 0 à 7 de haut en bas
        end_reine_y   =  button_clicked[1] // SQUARE_SIZE
        dist_reine_x  = end_reine_x - start_reine_x
        dist_reine_y  = end_reine_y - start_reine_y

        # Droite
        if dist_reine_x > 0 and button_clicked[1] == prev_pos[1]:
            for reine_step in range(1, abs(dist_reine_x), 1):
                case_index = liste_buttons.index(prev_pos_ob) + reine_step
                case = liste_buttons[case_index]
                if chessboard[case] is not None:
                    return False
            return True
        
        # Gauche
        elif dist_reine_x < 0 and button_clicked[1] == prev_pos[1]:
            for reine_step in range (1, abs(dist_reine_x), 1):
                case_index = liste_buttons.index(prev_pos_ob) - reine_step
                case = liste_buttons[case_index]
                if chessboard[case] is not None:
                    return False
            return True
              
        # Haut
        elif dist_reine_y < 0 and button_clicked[0] == prev_pos[0]:
            for reine_step in range (1, abs(dist_reine_y), 1):
                case_index = liste_buttons.index(prev_pos_ob) + reine_step * BOARD_L
                case = liste_buttons[case_index]
                if chessboard[case] is not None:
                    return False
            return True
        
        # Bas
        elif dist_reine_y > 0 and button_clicked[0] == prev_pos[0]:
            for reine_step in range (1, abs(dist_reine_y), 1):
                case_index = liste_buttons.index(prev_pos_ob) - reine_step * BOARD_L
                case = liste_buttons[case_index]
                if chessboard[case] is not None:
                    return False
            return True
        
        elif abs(dist_reine_x) == abs(dist_reine_y):
            # Haut droite
            if dist_reine_x > 0 and dist_reine_y < 0:
                for reine_step in range(1, abs(dist_reine_x),1):
                    case_index = liste_buttons.index(prev_pos_ob) + reine_step + reine_step*BOARD_L
                    case = liste_buttons[case_index]
                    if chessboard[case] is not None:
                        return False
                return True
            # Haut gauche
            elif dist_reine_x < 0 and dist_reine_y < 0:
                for reine_step in range(1, abs(dist_reine_x),1):
                    case_index = liste_buttons.index(prev_pos_ob) - reine_step + reine_step*BOARD_L
                    case = liste_buttons[case_index]
                    if chessboard[case] is not None:
                        return False
                return True
            # Bas droite
            elif dist_reine_x > 0 and dist_reine_y > 0:
                for reine_step in range(1, abs(dist_reine_x),1):
                    case_index = liste_buttons.index(prev_pos_ob) + reine_step - reine_step*BOARD_L
                    case = liste_buttons[case_index]
                    if chessboard[case] is not None:
                        return False
                return True
            # Bas gauche
            elif dist_reine_x < 0 and dist_reine_y > 0:
                for reine_step in range(1, abs(dist_reine_x),1):
                    case_index = liste_buttons.index(prev_pos_ob) - reine_step - reine_step*BOARD_L
                    case = liste_buttons[case_index]
                    if chessboard[case] is not None:
                        return False
                return True
            
    if piece_type == 'Roi':
        start_roi_x = prev_pos[0] // SQUARE_SIZE
        start_roi_y = prev_pos[1] // SQUARE_SIZE
        # 0 à 7 de gauche à droite
        end_roi_x   = button_clicked[0] // SQUARE_SIZE
        # 0 à 7 de haut en bas
        end_roi_y   =  button_clicked[1] // SQUARE_SIZE
        dist_roi_x  = end_roi_x - start_roi_x
        dist_roi_y  = end_roi_y - start_roi_y

        if abs(dist_roi_x) <= 1 and abs(dist_roi_y) <= 1:

            # Droite
            if dist_roi_x == 1 and dist_roi_y == 0:
                return True
            
            # Gauche
            elif dist_roi_x == -1 and dist_roi_y == 0:
                return True
            
            # Haut
            elif dist_roi_x == 0 and dist_roi_y == -1:
                return True
            
            # Bas
            elif dist_roi_x == 0 and dist_roi_y == 1:
                return True
            
            # Haut droite
            elif dist_roi_x ==  1 and dist_roi_y == -1:
                return True
            
            # Haut gauche
            elif dist_roi_x == -1 and dist_roi_y == -1:
                return True
            
            # Bas droite
            elif dist_roi_x == 1 and dist_roi_y == 1:
                return True
            
            # Bas gauche
            elif dist_roi_x == -1 and dist_roi_y ==1:
                return True

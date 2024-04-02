from CommonValues import * 
from GetChessNotation import get_chess_notation
from Classes import *
from ButtonGen import *

def populate_board(liste_buttons):
    # Association des cases aux pièces (None ici car aucunes pièces au départ)
    # pour la suite voir fin de la fonction populate_board()
    print(liste_buttons)
    for board in range(64):
        nom_board = get_chess_notation(board) ; nom_board_o = liste_buttons[board]
        chessboard.update({nom_board_o:None})

    for pion in range(2):
        nom_button = None
        clr = color_team[pion]
        print(clr)
        path = None
        for team in range(8):
            if clr==W : nom_button = f'button{get_chess_notation(BOARD_L+team)}'             ; path = 'piw.png'
            else :      nom_button = f'button{get_chess_notation(BOARD_A - 2*BOARD_L+team)}' ; path = 'pib.png'
            coord_piece = globals()[nom_button].rect.center
            nom_piece = f'{clr}pion{team}' ; globals()[nom_piece] = Pion(color_team[pion], path) ; globals()[nom_piece].move(coord_piece)
            liste_sprite_pieces.append(globals()[nom_piece])
            noms_sprites.append(nom_piece)

    for tour in range(2):
        clr = color_team[tour]
        for team in range(2):
           if clr==W : nom_button = f'button{get_chess_notation(0+team*(BOARD_L-1))}'       ; path = 'tow.png'
           else :      nom_button = f'button{get_chess_notation(56+team*(BOARD_L-1))}'      ; path = 'tob.png'
           coord_piece = globals()[nom_button].rect.center
           nom_piece = f'{clr}tour{team}' ; globals()[nom_piece] = Tour(color_team[tour], path) ; globals()[nom_piece].move(coord_piece)
           liste_sprite_pieces.append(globals()[nom_piece])
           noms_sprites.append(nom_piece)

    for caval in range(2):
        clr = color_team[caval]
        for team in range(2):
           if clr==W : nom_button = f'button{get_chess_notation(1+team*(BOARD_L-3))}'       ; path = 'caw.png'
           else :      nom_button = f'button{get_chess_notation(57+team*(BOARD_L-3))}'      ; path = 'cab.png'
           coord_piece = globals()[nom_button].rect.center
           nom_piece = f'{clr}cavalier{team}' ; globals()[nom_piece] = Cavalier(color_team[caval], path) ; globals()[nom_piece].move(coord_piece)
           liste_sprite_pieces.append(globals()[nom_piece])
           noms_sprites.append(nom_piece)

    for fou in range(2):
        clr = color_team[fou]
        for team in range(2):
           if clr==W : nom_button = f'button{get_chess_notation(2+team*(BOARD_L-5))}'       ; path = 'fow.png'
           else :      nom_button = f'button{get_chess_notation(58+team*(BOARD_L-5))}'      ; path = 'fob.png'
           coord_piece = globals()[nom_button].rect.center
           nom_piece = f'{clr}fou{team}' ; globals()[nom_piece] = Fou(color_team[fou], path) ; globals()[nom_piece].move(coord_piece)
           liste_sprite_pieces.append(globals()[nom_piece])
           noms_sprites.append(nom_piece)

    for reine in range(2):
        clr = color_team[reine]
        if clr==W : nom_button = f'button{get_chess_notation(3)}'  ; path = 'rew.png'
        else :      nom_button = f'button{get_chess_notation(59)}' ; path = 'reb.png'
        coord_piece = globals()[nom_button].rect.center
        nom_piece = f'{clr}reine0' ; globals()[nom_piece] = Reine(color_team[reine], path) ; globals()[nom_piece].move(coord_piece)
        liste_sprite_pieces.append(globals()[nom_piece])
        noms_sprites.append(nom_piece)

    for roi in range(2):
        clr = color_team[roi]
        if clr==W : nom_button = f'button{get_chess_notation(4)}'  ; path = 'row.png'
        else :      nom_button = f'button{get_chess_notation(60)}' ; path = 'rob.png'
        coord_piece = globals()[nom_button].rect.center
        nom_piece = f'{clr}roi0' ; globals()[nom_piece] = Roi(color_team[roi], path) ; globals()[nom_piece].move(coord_piece)
        liste_sprite_pieces.append(globals()[nom_piece])
        noms_sprites.append(nom_piece)

    # Suite du dico, comparaison de chaque coordonnées de case avec chaque coordonnées de pièce
    # Si mêmes coordonnées alors association des deux dans le dico chessboard{},
    # Pour mieux voir l'effet dans la console, remplacer dans chessboard.update
    #   nom_case_ob  par  nom_case  et  comp_piece  par  nom_piece_solo  merci de bien remettre après
 
    for case in range(64):
        nom_case = get_chess_notation(case) ; nom_case_ob = liste_buttons[case]
        for piece in range(len(noms_sprites)):
            nom_piece_solo = noms_sprites[piece]
            comp_piece=liste_sprite_pieces[piece]
            if comp_piece.rect.center == nom_case_ob.rect.center:
                print(f'{nom_piece_solo} est en case {nom_case}')
                chessboard.update({nom_case_ob:comp_piece})
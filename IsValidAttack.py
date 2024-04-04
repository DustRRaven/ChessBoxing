from CommonValues import *
import IsValidMove

def test(button_clicked = tuple, prev_pos = tuple, piece = object):
    prev_piece = chessboard[button_clicked]
    #print(prev_piece)
    chessboard[button_clicked] = None
    piece_type = (type(piece).__name__)
    if piece_type != 'Pion':
        if IsValidMove.test(button_clicked, prev_pos, piece) == True:
            if prev_piece.color == B:
                B_dead_pieces.append(prev_piece)
            else: W_dead_pieces.append(prev_piece)
            return True
        else:
            chessboard[button_clicked] = prev_piece
            
    else:
        if IsValidMove.test(button_clicked, prev_pos, piece) == 12:
            if prev_piece.color == W:
                W_dead_pieces.append(prev_piece)
            else: B_dead_pieces.append(prev_piece)
            return True
        else: chessboard[button_clicked] = prev_piece




## Affiche les pièces mortes sur le côté
def dead_display(dead_piece):
    global dead_counters
    global coord_dead_pieces
    t_piece = type(dead_piece).__name__
    
    coord_piece = coord_dead_pieces[t_piece][dead_piece.color]

    if t_piece == 'Pion':
        if dead_piece.color == B:
            dead_counters[t_piece][dead_piece.color] +=1
            if t_piece in B_type_dead:
                liste_sprite_pieces.pop(liste_sprite_pieces.index(dead_piece))
            else:
                dead_piece.move(coord_piece)
                B_type_dead.append(t_piece)

        else:
            dead_counters[t_piece][dead_piece.color] +=1
            if t_piece in W_type_dead:
                liste_sprite_pieces.pop(liste_sprite_pieces.index(dead_piece))
            else:
                dead_piece.move(coord_piece)
                W_type_dead.append(t_piece)
    
    elif t_piece == 'Tour':
        if dead_piece.color == B:
            dead_counters[t_piece][dead_piece.color] +=1
            if t_piece in B_type_dead:
                liste_sprite_pieces.pop(liste_sprite_pieces.index(dead_piece))
            else:
                dead_piece.move(coord_piece)
                B_type_dead.append(t_piece)
        else:
            dead_counters[t_piece][dead_piece.color] +=1
            if t_piece in W_type_dead:
                liste_sprite_pieces.pop(liste_sprite_pieces.index(dead_piece))
            else:
                dead_piece.move(coord_piece)
                W_type_dead.append(t_piece)
    
    elif t_piece == 'Cavalier':
        if dead_piece.color == B:
            dead_counters[t_piece][dead_piece.color] +=1
            if t_piece in B_type_dead:
                liste_sprite_pieces.pop(liste_sprite_pieces.index(dead_piece))
            else:
                dead_piece.move(coord_piece)
                B_type_dead.append(t_piece)
        else:
            dead_counters[t_piece][dead_piece.color] +=1
            if t_piece in W_type_dead:
                liste_sprite_pieces.pop(liste_sprite_pieces.index(dead_piece))
            else:
                dead_piece.move(coord_piece)
                W_type_dead.append(t_piece)

    elif t_piece == 'Fou':
        if dead_piece.color == B:
            dead_counters[t_piece][dead_piece.color] +=1
            if t_piece in B_type_dead:
                liste_sprite_pieces.pop(liste_sprite_pieces.index(dead_piece))
            else:
                dead_piece.move(coord_piece)
                B_type_dead.append(t_piece)
        else:
            dead_counters[t_piece][dead_piece.color] +=1
            if t_piece in W_type_dead:
                liste_sprite_pieces.pop(liste_sprite_pieces.index(dead_piece))
            else:
                dead_piece.move(coord_piece)
                W_type_dead.append(t_piece)
    
    elif t_piece == 'Reine':
        if dead_piece.color == B:
            if t_piece in B_type_dead:
                liste_sprite_pieces.pop(liste_sprite_pieces.index(dead_piece))
            else:
                dead_piece.move(coord_piece)
                B_type_dead.append(t_piece)
        else:
            if t_piece in W_type_dead:
                liste_sprite_pieces.pop(liste_sprite_pieces.index(dead_piece))
            else:
                dead_piece.move(coord_piece)
                W_type_dead.append(t_piece)
    
    elif t_piece == 'Roi':
        if dead_piece.color == B:
            if t_piece in B_type_dead:
                liste_sprite_pieces.pop(liste_sprite_pieces.index(dead_piece))
            else:
                dead_piece.move(coord_piece)
                B_type_dead.append(t_piece)
        else:
            if t_piece in W_type_dead:
                liste_sprite_pieces.pop(liste_sprite_pieces.index(dead_piece))
            else:
                dead_piece.move(coord_piece)
                W_type_dead.append(t_piece)

def dead_counter():
    type_piece = ['Pion', 'Tour', 'Cavalier', 'Fou']
    for t_piece in type_piece:
        for color in color_team:
            if dead_counters[t_piece][color] > 1:
                font_counter = pygame.font.Font(None, 24)
                text_surface = font_counter.render(str(f'x{dead_counters[t_piece][color]}'), True, RED)
                text_rect = text_surface.get_rect()
                text_rect.bottomleft = ((coord_dead_pieces[t_piece][color])[0] +20, (coord_dead_pieces[t_piece][color])[1])
                
                screen.blit(text_surface, text_rect)
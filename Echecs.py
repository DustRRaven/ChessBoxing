import pygame
from pygame.locals import *
import sys
import os
from CommonValues import *
import IsValidMove
import IsValidAttack
from Classes import *
from GetChessNotation import get_chess_notation
from ButtonGen import ButtonGen



## pygame setup, les valeurs se trouve dans CommonValues
pygame.init()
pygame.display.set_caption('Echecs')

def afficher_message(message):
    fenetre.fill(BLACK)  # Efface l'écran
    texte = font.render(message, True, WHITE)
    texte_rect = texte.get_rect(center=(400, 300))
    fenetre.blit(texte, texte_rect)
    pygame.display.flip()  # Rafraîchit l'affichage
    print(message)

def draw_board():
    for row in range(8):
        for col in range(8):
            color = BEIGE if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

ButtonGen()
from PopulateBoard import populate_board

class Jeu:
    def __init__(self):
        None
print(liste_buttons)
populate_board(liste_buttons)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Test des mouvements
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(64):
                    button_id = liste_buttons[i]
                    nom_button = get_chess_notation(i)
                    if button_id.rect.collidepoint(event.pos):
                          
                        if len(selected_piece) == 0 and chessboard[button_id] != None and chessboard[button_id].color == current_player:
                            previous_pos = button_id ; selected_piece.append(chessboard[button_id]) ; selected_piece[0].selected = True
                            print('choix piece') ; print(f'liste piece selectionnée{selected_piece}') ; print(f'dico board{chessboard[button_id]}')
                            
                        elif len(selected_piece) == 0 and chessboard[button_id] == None:
                            print('case vide')
                            
                        elif len(selected_piece) == 0 and chessboard[button_id].color != current_player:
                            print('case ennemie')
                            
                        elif len(selected_piece) == 1 and chessboard[button_id] == None:
                            if IsValidMove.test(button_id, previous_pos, selected_piece[0]) == True:
                                print('mouvement')
                                if selected_piece[0].rect.center != button_id.rect.center:
                                    selected_piece[0].move(button_id.rect.center)
                                    chessboard[button_id] = selected_piece[0]
                                    chessboard[previous_pos] = None
                                    print(f'liste piece selectionnée{selected_piece}')
                                    selected_piece[0].selected = False
                                    selected_piece.pop()
                                    print(f'liste piece selectionnée{selected_piece}')
                                            
                                    if current_player == W : current_player = B ; print(current_player)
                                    else: current_player = W ; tour +=1 ; print(f'{current_player} ;',f'tour: {tour}')
                                    
                                else: selected_piece[0].selected = False ; selected_piece.pop()
                            else: selected_piece[0].selected = False ; selected_piece.pop()

                        ## Test si attaque possible
                        elif len(selected_piece) == 1 and chessboard[button_id] != None and chessboard[button_id].color != selected_piece[0].color:
                            if IsValidAttack.test(button_id, previous_pos, selected_piece[0]) == True:
                                selected_piece[0].move(button_id.rect.center)
                                chessboard[button_id] = selected_piece[0]
                                chessboard[previous_pos] = None
                                selected_piece[0].selected =  False
                                selected_piece.pop()

                                if current_player == W : current_player = B ; print(current_player)
                                else: current_player = W ; tour +=1 ; print(f'{current_player} ;',f'tour: {tour}')

                        elif len(selected_piece) == 1 and chessboard[button_id] != None and chessboard[button_id].color == selected_piece[0].color:
                            selected_piece[0].selected = False ; selected_piece.pop()
                        
                        
    pygame.display.flip()
    draw_board()
    
    for sprite in liste_sprite_pieces:
        sprite.draw()
    
    clock.tick(60)

pygame.quit()
sys.exit()
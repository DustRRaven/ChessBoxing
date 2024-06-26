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
import IsCheckMate



## pygame setup, les valeurs se trouve dans CommonValues
pygame.init()
pygame.display.set_caption('Echecs')

def afficher_message(message, color):
    if color == B:
        fenetre.fill(BLACK)  # Efface l'écran
        texte = font_timer.render(message, True, WHITE)
        texte_rect = texte.get_rect(center=(WIDTH//2,HEIGHT//2))
        fenetre.blit(texte, texte_rect)
        pygame.display.flip()  # Rafraîchit l'affichage
    
    else:
        fenetre.fill(WHITE)  # Efface l'écran
        texte = font_timer.render(message, True, BLACK)
        texte_rect = texte.get_rect(center=(WIDTH//2,HEIGHT//2))
        fenetre.blit(texte, texte_rect)
        pygame.display.flip()  # Rafraîchit l'affichage

def gamedone(color):
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        afficher_message(f'{color} won', color)
        pygame.display.update()
        clock.tick(15)

        

    

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

populate_board(liste_buttons)

table = Background("table.jpg")
liste_sprite_other.append(table)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        # Test des mouvements
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(64):
                    button_id = liste_buttons[i]
                    piece = chessboard[button_id]
                    nom_button = get_chess_notation(i)
                    if button_id.rect.collidepoint(event.pos):
                          
                        if len(selected_piece) == 0 and chessboard[button_id] != None and chessboard[button_id].color == current_player:
                            previous_pos = button_id ; selected_piece.append(chessboard[button_id]) ; selected_piece[0].selected = True
                            print('choix piece')
                            
                        elif len(selected_piece) == 0 and chessboard[button_id] == None:
                            print('case vide')
                            
                        elif len(selected_piece) == 0 and chessboard[button_id].color != current_player:
                            print('case ennemie')
                            
                        elif len(selected_piece) == 1 and chessboard[button_id] == None:
                            if IsValidMove.test(button_id, previous_pos, selected_piece[0]) == True:
                                print('mouvement')
                                if selected_piece[0].rect.center != button_id.rect.center:
                                    pygame.mixer.Sound.play(move)
                                    selected_piece[0].move(button_id.rect.center)
                                    chessboard[button_id] = selected_piece[0]
                                    chessboard[previous_pos] = None
                                    selected_piece[0].selected = False
                                    selected_piece.pop()
                                            
                                    if current_player == W : current_player = B ; print(current_player)
                                    else: current_player = W ; tour +=1 ; print(f'{current_player} ;',f'tour: {tour}')
                                    
                                else: selected_piece[0].selected = False ; selected_piece.pop()
                            else: selected_piece[0].selected = False ; selected_piece.pop()

                        ## Test si attaque possible
                        elif len(selected_piece) == 1 and chessboard[button_id] != None and chessboard[button_id].color != selected_piece[0].color:
                            dead_piece = chessboard[button_id]
                            if IsValidAttack.test(button_id, previous_pos, selected_piece[0]) == True:
                                pygame.mixer.Sound.play(capture)
                                IsValidAttack.dead_display(dead_piece)
                                selected_piece[0].move(button_id.rect.center)
                                chessboard[button_id] = selected_piece[0]
                                chessboard[previous_pos] = None

                                


                                selected_piece[0].selected =  False
                                selected_piece.pop()

                                if current_player == W : current_player = B ; print(current_player)
                                else: current_player = W ; tour +=1 ; print(f'{current_player} ;',f'tour: {tour}')

                                

                        elif len(selected_piece) == 1 and chessboard[button_id] != None and chessboard[button_id].color == selected_piece[0].color:
                            selected_piece[0].selected = False ; selected_piece.pop()
                        
                        print(IsCheckMate.get_possible_moves(W))

                        if IsCheckMate.is_check(W, chessboard):
                                print('White in check')
                        elif IsCheckMate.is_check(B, chessboard):
                                print('Black in check')
                        if IsCheckMate.is_checkmate(W):
                            gamedone(W)
                        elif IsCheckMate.is_checkmate(B):
                            gamedone(B)

                ## Teste si un pion peut se changer en autre pièce
                if len(selected_piece) == 1 and type(selected_piece[0]).__name__ == 'Pion':
                    for dead_piece in W_dead_pieces:
                        if dead_piece.rect.collidepoint(event.pos) and selected_piece[0].color == W:
                            
                                W_dead_pieces.append(selected_piece[0])
                                dead_piece.move(selected_piece[0].rect.center)
                                selected_piece[0].selected = False

                                case_pion_switch = list(chessboard.keys())[list(chessboard.values()).index(selected_piece[0])]

                                chessboard[case_pion_switch] = dead_piece
                                IsValidAttack.dead_display(selected_piece[0])
                                selected_piece.pop()

                
                
        
    pygame.display.flip()
    draw_board()
    
    
    table.draw()

    for sprite in liste_sprite_pieces:
        sprite.draw()
    
    IsValidAttack.dead_counter()

    clock.tick(60)

#pygame.quit()

#sys.exit()
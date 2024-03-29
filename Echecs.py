import pygame
from pygame.locals import *
import sys
import os
import IsValidMove


## Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (107, 68, 35)
BEIGE = (205, 205, 180)
BLUE  = (90, 90 , 255)
RED   = (200,0,0)


W = 'W'
B = 'B'

color_team = [W, B]


## Définition des dimensions de la fenêtre, vérification que la variable SQUARE_SIZE sera impair pour avoir son centre parfait
WIDTH, HEIGHT = 800, 600
while min(WIDTH // 8, HEIGHT //8) % 2 != 1:
    if WIDTH < HEIGHT       : WIDTH -= 1
    elif WIDTH > HEIGHT     : HEIGHT -= 1
    else                    : WIDTH-=1 ; HEIGHT-=1

## Définition de la taille de la case et des variables désignant les mesures de l'échiquier

SQUARE_SIZE = min(WIDTH // 8, HEIGHT // 8)
EMPTY_WIDTH = WIDTH - HEIGHT

BOARD_L = 8
BOARD_A = 64


# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
tour = 1
current_player = B
pygame.display.set_caption('Echecs')
font = pygame.font.SysFont(None, 30)
fenetre = pygame.display.set_mode((WIDTH, HEIGHT))
sprites = pygame.sprite.Group()


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

class Button:
    def __init__(self,coordx,coordy,size=SQUARE_SIZE):
        self.surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        self.rect = self.surface.get_rect(center=(coordx,coordy))
        fenetre.blit(self.surface, self.rect)
        print(f'Button created at ({coordx}, {coordy}), rect: {self.rect.center}')

def get_chess_notation(i):
    lettres = ['A','B','C','D','E','F','G','H']
    nombres = ['1','2','3','4','5','6','7','8']
    chess_notation = []
    for lettre in lettres:
        for chiffre in nombres:
            chess_notation.append(lettre + chiffre)
    return chess_notation[i]

# Ne pas mettre ce qui suit dans une fonction, sinon les variables créées seront locales
liste_buttons = []
cpt_button = -1
for i in range(8):
    coordy = HEIGHT - i * SQUARE_SIZE - SQUARE_SIZE//2

    for j in range(8):
        cpt_button += 1
        coordx = j*SQUARE_SIZE + SQUARE_SIZE//2
        nom_button = f'button{get_chess_notation(cpt_button)}' ; globals()[nom_button] = Button(coordx,coordy)
        liste_buttons.append(globals()[nom_button])

# Balise du message au dessus
         

class Piece:
    def __init__(self, color, texture):
        self.color = color
        self.texture_path = os.path.join('images', texture)
        self.texture = pygame.image.load(self.texture_path)
        self.texture = pygame.transform.smoothscale(self.texture, (SQUARE_SIZE, SQUARE_SIZE))
        self.rect = self.texture.get_rect(center=(0, 0))
        self.selected = False

    def move(self, coord):
        self.rect.center = coord

    def draw(self):
        if self.selected:
            if self.color == W:
                pygame.draw.rect(fenetre, BLUE, self.rect.move(0,-1), 3)
            else: pygame.draw.rect(fenetre, RED, self.rect.move(0,-1), 3)
        fenetre.blit(self.texture, self.rect)

class Pion(Piece):
    def __init__(self, color, texture):
        super().__init__(color, texture)
    def move(self, coord):
        super().move(coord)      

class Tour(Piece):
    def __init__(self, color, texture):
        super().__init__(color, texture)
    def move(self, coord):
        super().move(coord)

    def move(self, coord):
        super().move(coord)

class Cavalier(Piece):
    def __init__(self, color, texture):
        super().__init__(color, texture)
    def move(self, coord):
        super().move(coord)

class Fou(Piece):
    def __init__(self, color, texture):
        super().__init__(color, texture)
    def move(self, coord):
        super().move(coord)

class Reine(Piece):
    def __init__(self, color, texture):
        super().__init__(color, texture)
    def move(self, coord):
        super().move(coord)

class Roi(Piece):
    def __init__(self, color, texture):
        super().__init__(color, texture)
    def move(self, coord):
        super().move(coord)


liste_sprite_pieces = []
noms_sprites  = []
chessboard = {}

def populate_board():
    # Association des cases aux pièces (None ici car aucunes pièces au départ)
    # pour la suite voir fin de la fonction populate_board()
    for board in range(64):
        nom_board = get_chess_notation(board) ; nom_board_o =  globals()['button' + nom_board]
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


class Jeu:
    def __init__(self):
        None

populate_board()
#print(chessboard)
selected_piece = []


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
                            if IsValidMove.test(SQUARE_SIZE, liste_buttons, chessboard, W, B, BOARD_L, button_id, previous_pos, selected_piece[0]) == True:
                                print('mouvement')
                                if selected_piece[0].rect.center != button_id.rect.center:
                                    selected_piece[0].move(button_id.rect.center)
                                    chessboard[button_id] = selected_piece[0]
                                    chessboard[previous_pos] = None
                                    print(f'liste piece selectionnée{selected_piece}')
                                    selected_piece[0].selected = False
                                    selected_piece.pop()
                                    print(f'liste piece selectionnée{selected_piece}')
                                    """        
                                    if current_player == W : current_player = B ; print(current_player)
                                    else: current_player = W ; tour +=1 ; print(f'{current_player} ;',f'tour: {tour}')
                                    """
                                else: selected_piece[0].selected = False ; selected_piece.pop()
                            else: selected_piece[0].selected = False ; selected_piece.pop()
                        elif len(selected_piece) == 1 and chessboard[button_id] != None and chessboard[button_id].color == selected_piece[0].color:
                            selected_piece[0].selected = False ; selected_piece.pop()
                        
                                
                        
                        

    pygame.display.flip()
    draw_board()
    
    for sprite in liste_sprite_pieces:
        sprite.draw()
    
    clock.tick(60)

pygame.quit()
sys.exit()
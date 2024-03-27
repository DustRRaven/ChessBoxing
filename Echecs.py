import pygame
from pygame.locals import *
import sys
import os

# Constantes



## Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (107, 68, 35)
BEIGE = (205, 205, 180)


W = 0
B = 1

colours = {B: BLACK, W: WHITE}



## Définition des dimensions de la fenêtre, vérification que la variable SQUARE_SIZE sera impair pour avoir son centre parfait
WIDTH, HEIGHT = 800, 600
while min(WIDTH // 8, HEIGHT //8) % 2 != 1:
    if WIDTH < HEIGHT       : WIDTH -= 1
    elif WIDTH > HEIGHT     : HEIGHT -= 1
    else                    : WIDTH-=1 ; HEIGHT-=1

## Définition de la taille de la case

SQUARE_SIZE = min(WIDTH // 8, HEIGHT // 8)
EMPTY_WIDTH = WIDTH - HEIGHT

## Inutile : TILESIZE  = 100
MAPWIDTH  = 8
MAPHEIGHT = 8


# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
tour = 0
current_player = W
pygame.display.set_caption('Echecs')
font = pygame.font.SysFont(None, 30)
fenetre = pygame.display.set_mode((WIDTH, HEIGHT))


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
        #self.surface.fill(GRAY)
        fenetre.blit(self.surface, self.rect)
        print(f'Button created at ({coordx}, {coordy}), rect: {self.rect}')


def get_chess_notation(i):
    lettres = ["A","B","C","D","E","F","G","H"]
    nombres = ["1","2","3","4","5","6","7","8"]
    chess_notation = []
    for lettre in lettres:
        for chiffre in nombres:
            chess_notation.append(lettre + chiffre)
    return chess_notation[i]


# Ne pas mettre ce qui suit dans une fonction, sinon les variables créées seront locales

cpt_button = -1
for i in range(8):
    coordy = HEIGHT - i * SQUARE_SIZE - SQUARE_SIZE//2

    for j in range(8):
        cpt_button += 1
        coordx = j*SQUARE_SIZE + SQUARE_SIZE//2
        nom_button = f'button{get_chess_notation(cpt_button)}' ; globals()[nom_button] = Button(coordx,coordy)

# Balise du message au dessus                              

def mouvement_légal(mouvement): #mouvement est un string contenant la position sur l'échiquier (comme get_chess_notation() )
    for i in range(64):
        if get_chess_notation(i) == mouvement:
            return True
    return False

class Piece:
    def __init__(self, color, texture):
        self.color = color
        self.texture_path = os.path.join("images", texture)


    def move(self, new_position):
        if mouvement_légal(new_position):
            if tour ==1



class Pion(Piece):
    def __init__(self, color, texture):
        super().__init__(color, texture)
        self.texture = pygame.image.load(self.texture_path)

    def move(self, new_position): # Un pion êut avancer de 1 ou 2 cases au premier tour, il peut aussi attaquer et prendre une pièce adverse dans un coin supérieur
        ()

class Tour(Piece):
    def __init__(self, color, texture):
        super().__init__(color, texture)
        self.texture = pygame.image.load(self.texture_path)

    def move(self, new_position):
        
        pass 

class Cavalier(Piece):
    def __init__(self, color, texture):
        super().__init__(color, texture)
        self.texture = pygame.image.load(self.texture_path)

    def move(self, new_position):
        pass

class Fou(Piece):
    def __init__(self, color, texture):
        super().__init__(color, texture)
        self.texture = pygame.image.load(self.texture_path)

    def move(self, new_position):
        pass

class Reine(Piece):
    def __init__(self, color, texture):
        super().__init__(color, texture)
        self.texture = pygame.image.load(self.texture_path)

    def move(self, new_position):
        pass
    
class Roi(Piece):
    def __init__(self, color, texture):
        super().__init__(color, texture)
        self.texture = pygame.image.load(self.texture_path)

    def move(self, new_position):
        pass
    

class Echiquier:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        self.populate_board()
    
    def populate_board(self):
   
        # Dictionnaire contenant les pièces de départ et leurs position
        
        for pion in range(7):
            nom_piece = f"Wpion{pion}"
            globals()[nom_piece] = Pion(W,)

            pass
        for tour in range(1):

            pass
        for caval in range(1):

            pass
        for fou in range(1):

            pass
        for roi in range(0):

            pass
        for reines in range(0):

            pass

        positions_pieces = {}       

        
    def mouvements(self, nouv_postion):
        self.position = nouv_postion
    
    def case_vide(self, pos):
        if pos == None:
            return True
        return False


class Jeu:
    def __init__(self):
        None

chessboard = {}
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(64):
                    nom_button = get_chess_notation(i)
                    if globals()['button' + nom_button].rect.collidepoint(event.pos):
                        afficher_message(f"La case {nom_button} a été cliqué!")
                        current_player = B if current_player == W else W
                    

    pygame.display.flip()
    draw_board()
    clock.tick(60)

pygame.quit()
sys.exit()
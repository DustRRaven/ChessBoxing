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
current_player = W
pygame.display.set_caption('Echecs')
font = pygame.font.SysFont(None, 30)
fenetre = pygame.display.set_mode((WIDTH, HEIGHT))



def position_piece(piece, abscisse, ordonnee):
    if abscisse <= 7 or ordonnee <= 7:
        piece[0] = abscisse*(800/8)
        piece[1] = ordonnee*(600/8)
    if abscisse > 7 or ordonnee > 7:
        print("Erreur de données en ordonnee et/ou en abscisse")
        piece[0] = 0
        piece[1] = 0

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

class Piece:
    def __init__(self, color, texture):
        self.color = color
        self.texture_path = os.path.join("images", texture)


    def move(self, new_position):
        
        pass


class Pion(Piece):
    def __init__(self, color, texture):
        super().__init__(color, texture)
        self.texture = pygame.image.load(self.texture_path)

    def move(self, new_position):
        
        pass
        
        

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
        starting_pieces = {}    
        pass

    def mouvements(self, nouv_postion):
        self.position = nouv_postion
    
    def case_vide(self, pos):
        if pos == None:
            return True
        return False


class Jeu:
    def __init__(self):
        None

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
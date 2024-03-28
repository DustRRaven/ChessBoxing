import pygame
from pygame.locals import *
import sys
import os


## Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (107, 68, 35)
BEIGE = (205, 205, 180)


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
tour = 0
current_player = W
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
        self.texture = pygame.image.load(self.texture_path)
        self.texture = pygame.transform.smoothscale(self.texture, (SQUARE_SIZE, SQUARE_SIZE))
        self.rect = self.texture.get_rect(center=(0, 0))


    def move(self, coord):
        self.rect.center = coord
        pass

    def draw(self):
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
    
liste_sprites = []
noms_sprites  = []

def populate_board():
    # Dictionnaire contenant les pièces de départ et leurs position
    
    for pion in range(2):
        nom_button = None
        clr = color_team[pion]
        path = None
        for team in range(8):
            if clr==0:  nom_button = f'button{get_chess_notation(BOARD_L+team)}'             ; path = "piw.png"
            else:       nom_button = f'button{get_chess_notation(BOARD_A - 2*BOARD_L+team)}' ; path = "pib.png"
            coord_piece = globals()[nom_button].rect.center
            nom_piece = f"{clr}pion{team}" ; globals()[nom_piece] = Pion(W, path) ; globals()[nom_piece].move(coord_piece)
            liste_sprites.append(globals()[nom_piece])
            noms_sprites.append(nom_piece)
    print(noms_sprites)
    
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

    
    #positions_pieces = {}
    


class Jeu:
    def __init__(self):
        None

chessboard = {}

populate_board()

#print(liste_sprites)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(64):
                    nom_button = get_chess_notation(i)
                    if globals()['button' + nom_button].rect.collidepoint(event.pos):
                        afficher_message(f"La case {nom_button}, ({i}) a été cliqué!")
                        current_player = B if current_player == W else W
                    

    pygame.display.flip()
    draw_board()
    
    
    for sprite in liste_sprites:
        sprite.draw()
    
    clock.tick(60)

pygame.quit()
sys.exit()
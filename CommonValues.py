import pygame
import os
## Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (107, 68, 35)
BEIGE = (205, 205, 180)
BLUE  = (90, 90 , 255)
RED   = (200,0,0)
MAROON = (183, 65, 14)

## Définition des équipes
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


## Définition des valeurs dont pygame à besoin
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
tour = 1
current_player = W

font_timer = pygame.font.SysFont(None, 30)

fenetre = pygame.display.set_mode((WIDTH, HEIGHT))
sprites = pygame.sprite.Group()

## Définitions des listes et dico utilisés
liste_sprite_pieces = []
liste_sprite_other = []
noms_sprites  = []
chessboard = {}
liste_buttons = []
selected_piece = []
W_dead_pieces = []
B_dead_pieces = []
W_type_dead = []
B_type_dead = []

## Audio

move = pygame.mixer.Sound(os.path.join('audio', "move.wav"))
capture = pygame.mixer.Sound(os.path.join('audio', "capture.wav"))

## Dead counters
dead_counters = {
    'Pion': {'W': 0, 'B': 0},
    'Tour': {'W': 0, 'B': 0},
    'Cavalier': {'W': 0, 'B': 0},
    'Fou': {'W': 0, 'B': 0}
}

coord_dead_pieces = {
    'Pion': {'W': (8*SQUARE_SIZE+SQUARE_SIZE//2,HEIGHT-(SQUARE_SIZE//2)), 'B': (8*SQUARE_SIZE+SQUARE_SIZE//2,SQUARE_SIZE//2)},
    'Tour': {'W': (9*SQUARE_SIZE+SQUARE_SIZE//2,HEIGHT-(SQUARE_SIZE//2)), 'B': (9*SQUARE_SIZE+SQUARE_SIZE//2,SQUARE_SIZE//2)},
    'Cavalier': {'W': (8*SQUARE_SIZE+SQUARE_SIZE//2,HEIGHT-(SQUARE_SIZE+SQUARE_SIZE//2)), 'B': (8*SQUARE_SIZE+SQUARE_SIZE//2,SQUARE_SIZE+SQUARE_SIZE//2)},
    'Fou': {'W': (9*SQUARE_SIZE+SQUARE_SIZE//2,HEIGHT-(SQUARE_SIZE+SQUARE_SIZE//2)), 'B': (9*SQUARE_SIZE+SQUARE_SIZE//2,SQUARE_SIZE+SQUARE_SIZE//2)},
    'Reine' : {'W': (8*SQUARE_SIZE+SQUARE_SIZE//2,HEIGHT-(2*SQUARE_SIZE+SQUARE_SIZE//2)), 'B': (8*SQUARE_SIZE+SQUARE_SIZE//2,2*SQUARE_SIZE+SQUARE_SIZE//2)},
    'Roi' : {'W': (9*SQUARE_SIZE+SQUARE_SIZE//2,HEIGHT-(2*SQUARE_SIZE+SQUARE_SIZE//2)), 'B': (9*SQUARE_SIZE+SQUARE_SIZE//2,2*SQUARE_SIZE+SQUARE_SIZE//2)}
}
import pygame
from pygame.locals import *
import sys

# Constantes

ROUGE = (255, 0, 0)

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
tour = 1
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
        self.rect = self.surface.get_rect(bottomleft=(coordx,coordy))
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
    coordy = HEIGHT - i * SQUARE_SIZE

    for j in range(8):
        cpt_button += 1
        coordx = SQUARE_SIZE*j
        nom_button = f'button{get_chess_notation(cpt_button)}' ; globals()[nom_button] = Button(coordx,coordy)

# Balise du message au dessus                              

class Piece:
    def __init__(self, color):
        self.color = color

class Pion:
    def __init__(self, color, position):
        super().__init__(color)
        self.position = position #position  == [axe des y, axe des x]
        #self.image = pygame.image.load(f'images/{color}_pawn.png')
    def mouvements_pion(self, nouv_position):
        if Echiquier.case_vide(nouv_position):
            if self.color == 'white':
                if tour == 1: #on ne peut aller que devant et on peut avancer de 1 ou 2 cases au tour 1
                    if nouv_position == ([2],self.position[1]) or nouv_position == ([3],self.position[1]) :
                        self.position = nouv_position
                else:  #si on est pas au tour 1
                    if nouv_position == (self.position[0]+1,self.position[1]): #cas ou on veut juste avancer d'une case
                        self.position = nouv_position
                    if nouv_position == (self.position[0]+1,self.position[1]-1) or (self.position[0]+1,self.position[1]+1): #cas ou on veut prendre une piece
                        # si éqyuipe adverse on rpend le pion  nouv position
                        if self.color not in Echiquier.self.board[nouv_position[0],[nouv_position[1]]]:
                            self.board[nouv_position[0], nouv_position[1]] = Pion(self.color, nouv_position)                          
                            self.board[self.position[0], self.position[1]] = None
            else:
                if tour == 1: #on ne peut aller que devant et on peut avancer de 1 ou 2 cases au tour 1
                    if nouv_position == ([5],self.position[1]) or nouv_position == ([4],self.position[1]) :
                        self.position = nouv_position
                else:  #si on est pas au tour 1
                    if nouv_position == (self.position[0]-1,self.position[1]): #cas ou on veut juste avancer d'une case
                        self.position = nouv_position
                    if nouv_position == (self.position[0]-1,self.position[1]-1) or (self.position[0]-1,self.position[1]+1): #cas ou on veut prendre une piece
                        # si éqyuipe adverse on rpend le pion  nouv position
                        if self.color not in Echiquier.self.board[nouv_position[0],[nouv_position[1]]]:
                            self.board[nouv_position[0], nouv_position[1]] = Pion(self.color, nouv_position)
                            self.board[self.position[0], self.position[1]] = None


class Tour:
    def __init__(self, color, position):
        super().__init__(color)
        #self.image = pygame.image.load(f'images/{color}_pawn.png')

class Cavalier:
    def __init__(self, color, ):
        super().__init__(color)
        #self.image = pygame.image.load(f'images/{color}_pawn.png')

class Fou:
    def __init__(self, color):
        super().__init__(color)
        #self.image = pygame.image.load(f'images/{color}_pawn.png')

class Reine:
    def __init__(self, color):
        super().__init__(color)
        #self.image = pygame.image.load(f'images/{color}_pawn.png')

    
class Fou:
    def __init__(self, color):
        super().__init__(color)
        #self.image = pygame.image.load(f'images/{color}_pawn.png')


class Roi:
    def __init__(self, color):
        super().__init__(color)
        #self.image = pygame.image.load(f'images/{color}_pawn.png')
    

class Echiquier:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        self.populate_board()
    def populate_board(self):
        # Initialise les positions de départ
        for i in range(8):
            self.board[1][i] = Pion('white',[0][i])
            self.board[6][i] = Pion('black', [6][i])
        self.board[0][0] = Tour('white',([0][0]))
        self.board[7][0] = Tour('black', ([7][0]))
        self.board[7][1] = Cavalier('black',([7][1]))
        self.board[7][6] = Cavalier('black',([7][6]))
        self.board[0][1] = Cavalier('white',([0][1]))
        self.board[0][6] = Cavalier('white',([0][6]))
        self.board[0][2] = Fou('white',([0][2]))
        self.board[0][5] = Fou('white',([0][5]))
        self.board[7][2] = Fou('black',([7][2]))
        self.board[7][5] = Fou('black',([7][5]))
        self.board[7][4] = Roi('black',([7][4]))
        self.board[0][4] = Roi('white',([0][4]))
        self.board[7][3] = Reine('black',([7][3]))
        self.board[0][3] = Reine('white',([0][3]))
        

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
                    if globals()['button' + nom_button].rect.collidepoint(event.pos): afficher_message(f"La case {nom_button} a été cliqué!")
                    

    pygame.display.flip()
    draw_board()
    clock.tick(60)

pygame.quit()
sys.exit()
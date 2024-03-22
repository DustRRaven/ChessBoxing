import pygame
from pygame.locals import *
import sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0
tour = 1
pygame.display.set_caption('Echecs')
font = pygame.font.SysFont(None, 30)
ROUGE = (255, 0, 0)

BLACK = (150,   150,   150  )
WHITE  = (255,   255,   255)
W = 0
B = 1
colours =   {
                B  : BLACK,
                W : WHITE,
            }


            





# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Définition des dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600

# Définition de la taille de la case
SQUARE_SIZE = HEIGHT // 8










TILESIZE  = 100
MAPWIDTH  = 8
MAPHEIGHT = 8

''' Initialisation des images png de pion'''
fenetre = pygame.display.set_mode((800, 600))
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)




pioni = pygame.image.load('images/pion.png').convert_alpha()
pion = [0,0]
fenetre.blit(pioni, (pion[0], pion[1]))

reinei = pygame.image.load("images/reine.png").convert_alpha()
reine = [0,0]
fenetre.blit(reinei, (reine[0], reine[1]))

roii = pygame.image.load("images/roi.png").convert_alpha()
roi = [0,0]
fenetre.blit(roii, (roi[0], roi[1]))

touri = pygame.image.load("images/tour.png").convert_alpha()
tour = [0,0]
fenetre.blit(touri, (tour[0], tour[1]))

chavalieri = pygame.image.load("images/cavalier.png").convert_alpha()
chavalier = [0,0]
fenetre.blit(chavalieri, (chavalier[0], chavalier[1]))

foui = pygame.image.load("images/fou.png").convert_alpha()
fou = [0,0]
fenetre.blit(foui, (fou[0], fou[1]))

touri2 = pygame.image.load("images/tour.png").convert_alpha()
tour2 = [0,0]
fenetre.blit(touri2, (tour2[0], tour2[1]))

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
            color = WHITE if (row + col) % 2 == 0 else GRAY
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


button_surface1 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface1.fill(GRAY)
button_rect1 = button_surface1.get_rect(bottomleft=(0,600))

button_surface2 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface2.fill(WHITE)
button_rect2 = button_surface2.get_rect(bottomleft=(75,600))

button_surface3 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface3.fill(GRAY)
button_rect3 = button_surface3.get_rect(bottomleft=(150,600))

button_surface4 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface4.fill(WHITE)
button_rect4 = button_surface4.get_rect(bottomleft=(225,600))

button_surface5 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface5.fill(GRAY)
button_rect5 = button_surface5.get_rect(bottomleft=(300,600))

button_surface6 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface6.fill(WHITE)
button_rect6 = button_surface6.get_rect(bottomleft=(375,600))

button_surface7 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface7.fill(GRAY)
button_rect7 = button_surface7.get_rect(bottomleft=(450,600))

button_surface8 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface8.fill(WHITE)
button_rect8 = button_surface8.get_rect(bottomleft=(525,600))

button_surface9 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface9.fill(WHITE)
button_rect9 = button_surface9.get_rect(bottomleft=(0,525))

button_surface10 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface10.fill(GRAY)
button_rect10 = button_surface10.get_rect(bottomleft=(75,525))

button_surface11 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface11.fill(WHITE)
button_rect11 = button_surface11.get_rect(bottomleft=(150,525))

button_surface12 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface12.fill(GRAY)
button_rect12 = button_surface12.get_rect(bottomleft=(225,525))

button_surface13 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface13.fill(WHITE)
button_rect13 = button_surface13.get_rect(bottomleft=(300,525))

button_surface14 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface14.fill(GRAY)
button_rect14 = button_surface14.get_rect(bottomleft=(375,525))

button_surface15 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface15.fill(WHITE)
button_rect15 = button_surface15.get_rect(bottomleft=(450,525))

button_surface16 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface16.fill(GRAY)
button_rect16 = button_surface16.get_rect(bottomleft=(525,525))


button_surface17 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface17.fill(GRAY)
button_rect17 = button_surface17.get_rect(bottomleft=(0,450))

button_surface18 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface18.fill(WHITE)
button_rect18 = button_surface18.get_rect(bottomleft=(75,450))

button_surface19 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface19.fill(GRAY)
button_rect19 = button_surface19.get_rect(bottomleft=(150,450))

button_surface20 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface20.fill(WHITE)
button_rect20 = button_surface20.get_rect(bottomleft=(225,450))

button_surface21 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface21.fill(GRAY)
button_rect21 = button_surface21.get_rect(bottomleft=(300,450))

button_surface22 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface22.fill(WHITE)
button_rect22 = button_surface22.get_rect(bottomleft=(375,450))

button_surface23 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface23.fill(GRAY)
button_rect23 = button_surface23.get_rect(bottomleft=(450,450))

button_surface24 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface24.fill(WHITE)
button_rect24 = button_surface24.get_rect(bottomleft=(525,450))

button_surface25 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface25.fill(WHITE)
button_rect25 = button_surface25.get_rect(bottomleft=(0,375))

button_surface26 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface26.fill(GRAY)
button_rect26 = button_surface26.get_rect(bottomleft=(75,375))

button_surface27 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface27.fill(WHITE)
button_rect27 = button_surface27.get_rect(bottomleft=(150,375))

button_surface28 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface28.fill(GRAY)
button_rect28 = button_surface28.get_rect(bottomleft=(225,375))

button_surface29 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface29.fill(WHITE)
button_rect29 = button_surface29.get_rect(bottomleft=(300,375))

button_surface30 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface30.fill(GRAY)
button_rect30= button_surface30.get_rect(bottomleft=(375,375))

button_surface31 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface31.fill(WHITE)
button_rect31 = button_surface31.get_rect(bottomleft=(450,375))

button_surface32 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface32.fill(GRAY)
button_rect32 = button_surface32.get_rect(bottomleft=(525,375))

button_surface33 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface33.fill(GRAY)
button_rect33 = button_surface33.get_rect(bottomleft=(0,300))

button_surface34 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface34.fill(WHITE)
button_rect34 = button_surface34.get_rect(bottomleft=(75,300))

button_surface35 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface35.fill(GRAY)
button_rect35 = button_surface35.get_rect(bottomleft=(150,300))

button_surface36 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface36.fill(WHITE)
button_rect36 = button_surface36.get_rect(bottomleft=(225,300))

button_surface37 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface37.fill(GRAY)
button_rect37 = button_surface37.get_rect(bottomleft=(300,300))

button_surface38 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface38.fill(WHITE)
button_rect38 = button_surface38.get_rect(bottomleft=(375,300))

button_surface39 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface39.fill(GRAY)
button_rect39 = button_surface39.get_rect(bottomleft=(450,300))

button_surface40 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface40.fill(WHITE)
button_rect40 = button_surface40.get_rect(bottomleft=(525,300))

button_surface41 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface41.fill(WHITE)
button_rect41 = button_surface41.get_rect(bottomleft=(0,225))

button_surface42 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface42.fill(GRAY)
button_rect42 = button_surface42.get_rect(bottomleft=(75,225))

button_surface43 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface43.fill(WHITE)
button_rect43 = button_surface43.get_rect(bottomleft=(150,225))

button_surface44 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface44.fill(GRAY)
button_rect44 = button_surface44.get_rect(bottomleft=(225,225))

button_surface45 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface45.fill(WHITE)
button_rect45 = button_surface45.get_rect(bottomleft=(300,225))

button_surface46 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface46.fill(GRAY)
button_rect46 = button_surface46.get_rect(bottomleft=(375,225))

button_surface47 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface47.fill(WHITE)
button_rect47 = button_surface47.get_rect(bottomleft=(450,225))

button_surface48 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface48.fill(GRAY)
button_rect48 = button_surface48.get_rect(bottomleft=(525,225))


button_surface49 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface49.fill(GRAY)
button_rect49 = button_surface49.get_rect(bottomleft=(0,150))

button_surface50 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface50.fill(WHITE)
button_rect50 = button_surface50.get_rect(bottomleft=(75,150))

button_surface51 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface51.fill(GRAY)
button_rect51 = button_surface51.get_rect(bottomleft=(150,150))

button_surface52 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface52.fill(WHITE)
button_rect52 = button_surface52.get_rect(bottomleft=(225,150))

button_surface53 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface53.fill(GRAY)
button_rect53 = button_surface53.get_rect(bottomleft=(300,150))

button_surface54 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface54.fill(WHITE)
button_rect54 = button_surface54.get_rect(bottomleft=(375,150))

button_surface55 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface55.fill(GRAY)
button_rect55 = button_surface55.get_rect(bottomleft=(450,150))

button_surface56 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface56.fill(WHITE)
button_rect56 = button_surface56.get_rect(bottomleft=(525,150))

button_surface57 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface57.fill(WHITE)
button_rect57 = button_surface57.get_rect(bottomleft=(0,75))

button_surface58 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface58.fill(GRAY)
button_rect58 = button_surface58.get_rect(bottomleft=(75,75))

button_surface59 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface59.fill(WHITE)
button_rect59 = button_surface59.get_rect(bottomleft=(150,75))

button_surface60 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface60.fill(GRAY)
button_rect60 = button_surface60.get_rect(bottomleft=(225,75))

button_surface61 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface61.fill(WHITE)
button_rect61 = button_surface61.get_rect(bottomleft=(300,75))

button_surface62 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface62.fill(GRAY)
button_rect62= button_surface62.get_rect(bottomleft=(375,75))

button_surface63 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface63.fill(WHITE)
button_rect63 = button_surface63.get_rect(bottomleft=(450,75))

button_surface64 = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
button_surface64.fill(GRAY)
button_rect64 = button_surface64.get_rect(bottomleft=(525,75))


                                
''''class Pion:
    def __init__(self, position, equipe):
        self.position = position
        self.equipe = equipe
    def mouvements(self, nouvelle_position, grille, dico_pos):
        if grille[nouvelle_position] != 0 :
            print("Position déja prise par une pièce")'''

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
            if self.color == 'white'
                if tour == 1: #on ne peut aller que devant et on peut avancer de 1 ou 2 cases au tour 1
                    if nouv_position == ([2],self.position[1]) or nouv_position == ([3],self.position[1]) :
                        self.position = nouv_position
                else:  #si on est pas au tour 1
                    if nouv_position == (self.position[0]+1,self.position[1]): #cas ou on veut juste avancer d'une case
                        self.position = nouv_position
                    if nouv_position == (self.position[0]+1,self.position[1]-1) or (self.position[0]+1,self.position[1]+1): #cas ou on veut prendre une piece
                        # si éqyuipe adverse on rpend le pion  nouv position
                        if self.color not in Echiquier.self.board[nouv_position[0],[nouv_position[1]]]:
                            self.board[nouv_position[0], nouv_position[1]] = Pion(self.color, nouv_position):
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
                            self.board[nouv_position[0], nouv_position[1]] = Pion(self.color, nouv_position):
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
        

    def draw_board():
        #construit l'échiquier sur la fenêtre
        for row in range(8):
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else GRAY
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
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
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button_rect1.collidepoint(event.pos):
            # Afficher un message lorsque le bouton est cliqué
                    afficher_message("Le bouton a été cliqué !")
    
    fenetre.blit(button_surface1, button_rect1)
    fenetre.blit(button_surface2, button_rect2)
    fenetre.blit(button_surface3, button_rect3)
    fenetre.blit(button_surface4, button_rect4)
    fenetre.blit(button_surface5, button_rect5)
    fenetre.blit(button_surface6, button_rect6)
    fenetre.blit(button_surface7, button_rect7)
    fenetre.blit(button_surface8, button_rect8)
    fenetre.blit(button_surface9, button_rect9)
    fenetre.blit(button_surface10, button_rect10)
    fenetre.blit(button_surface11, button_rect11)
    fenetre.blit(button_surface12, button_rect12)
    fenetre.blit(button_surface13, button_rect13)
    fenetre.blit(button_surface14, button_rect14)
    fenetre.blit(button_surface15, button_rect15)
    fenetre.blit(button_surface16, button_rect16)
    fenetre.blit(button_surface17, button_rect17)
    fenetre.blit(button_surface18, button_rect18)
    fenetre.blit(button_surface19, button_rect19)
    fenetre.blit(button_surface20, button_rect20)
    fenetre.blit(button_surface21, button_rect21)
    fenetre.blit(button_surface22, button_rect22)
    fenetre.blit(button_surface23, button_rect23)
    fenetre.blit(button_surface24, button_rect24)
    fenetre.blit(button_surface25, button_rect25)
    fenetre.blit(button_surface26, button_rect26)
    fenetre.blit(button_surface27, button_rect27)
    fenetre.blit(button_surface28, button_rect28)
    fenetre.blit(button_surface29, button_rect29)
    fenetre.blit(button_surface30, button_rect30)
    fenetre.blit(button_surface31, button_rect31)
    fenetre.blit(button_surface32, button_rect32)
    fenetre.blit(button_surface33, button_rect33)
    fenetre.blit(button_surface34, button_rect34)
    fenetre.blit(button_surface35, button_rect35)
    fenetre.blit(button_surface36, button_rect36)
    fenetre.blit(button_surface37, button_rect37)
    fenetre.blit(button_surface38, button_rect38)
    fenetre.blit(button_surface39, button_rect39)
    fenetre.blit(button_surface40, button_rect40)
    fenetre.blit(button_surface41, button_rect41)
    fenetre.blit(button_surface42, button_rect42)
    fenetre.blit(button_surface43, button_rect43)
    fenetre.blit(button_surface44, button_rect44)
    fenetre.blit(button_surface45, button_rect45)
    fenetre.blit(button_surface46, button_rect46)
    fenetre.blit(button_surface47, button_rect47)
    fenetre.blit(button_surface48, button_rect48)
    fenetre.blit(button_surface49, button_rect49)
    fenetre.blit(button_surface50, button_rect50)
    fenetre.blit(button_surface51, button_rect51)
    fenetre.blit(button_surface52, button_rect52)
    fenetre.blit(button_surface53, button_rect53)
    fenetre.blit(button_surface54, button_rect54)
    fenetre.blit(button_surface55, button_rect55)
    fenetre.blit(button_surface56, button_rect56)
    fenetre.blit(button_surface57, button_rect57)
    fenetre.blit(button_surface58, button_rect58)
    fenetre.blit(button_surface59, button_rect59)
    fenetre.blit(button_surface60, button_rect60)
    fenetre.blit(button_surface61, button_rect61)
    fenetre.blit(button_surface62, button_rect62)
    fenetre.blit(button_surface63, button_rect63)
    fenetre.blit(button_surface64, button_rect64)
    
    pygame.display.flip()
    draw_board()
    clock.tick(60)

    

pygame.quit()
sys.exit()


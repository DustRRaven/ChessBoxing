from CommonValues import *
import pygame
import os

class Button:
    def __init__(self,coordx,coordy,size=SQUARE_SIZE):
        self.surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        self.rect = self.surface.get_rect(center=(coordx,coordy))
        fenetre.blit(self.surface, self.rect)
        # print(f'Button created at ({coordx}, {coordy}), rect: {self.rect.center}')

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

class Background():
    def __init__(self,texture):
        self.texture_path = os.path.join('images', texture)
        self.texture = pygame.image.load(self.texture_path)
        self.texture = pygame.transform.smoothscale(self.texture, (EMPTY_WIDTH, HEIGHT))
        self.rect = self.texture.get_rect(topleft=(WIDTH-EMPTY_WIDTH,0))
    def draw(self):
        fenetre.blit(self.texture, self.rect)
import pygame as pg
from main import *

class Personnage:
    def __init__(self, image_path):
        self.image = pg.image.load(image_path)
        self.position = [6, 19]
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0] * CASE_SIZE  # Position initiale en pixels (6ème colonne)
        self.rect.y = self.position[1] * CASE_SIZE  # Position initiale en pixels (dernière ligne)

    def draw(self, window):
        window.blit(self.image, self.rect)

    def move(self, x, y):
        # Vérifier si le déplacement est valide
        new_x = self.rect.x + x
        new_y = self.rect.y + y
        if 0 <= new_x < WINDOW_SIZE[0] - self.rect.width and 0 <= new_y < WINDOW_SIZE[1] - self.rect.height:
            self.rect.x = new_x
            self.rect.y = new_y
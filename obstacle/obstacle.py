import pygame as pg
from typing import Tuple


class Obstacle(pg.sprite.Sprite):
    def __init__(self, x, y, obstacle_image):
        super(Obstacle, self).__init__()
        self.x = x
        self.y = y
        # tree_image = r".\images\tree.png"

        # Load the image, preserve alpha channel for transparency
        self.surf = pg.image.load(obstacle_image).convert_alpha()
        # Save the rect so you can move it
        self.rect = self.surf.get_rect()

    def update(self, screen, pos: Tuple):
        self.rect.center = pos
        # draw the image in the screen
        screen.blit(self.surf, self.rect)


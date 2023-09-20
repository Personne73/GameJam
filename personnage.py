import pygame as pg

class Personnage(object):
    def __init__(self):
        self.image = pg.image.load("mettre_chemin")
        self.position = [4, 4]
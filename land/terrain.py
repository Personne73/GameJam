import random
import pygame as pg
from enum import Enum
import os

class TypeTerrain(Enum):
    GRASS = 1
    ROAD = 2
    GLITCH = 3

class Cell():
    def __init__(self, type_terrain, obstacle=0):
        self.type_terrain = type_terrain
        self.obstacle = obstacle

class Terrain(object):
    # 20x14 blocks, dont 2 de bordure en largeur

    def __init__(self):
        self.tableau = [[]for j in range(20)]
        self.init_terrain()

        self.image_bush = pg.image.load(os.path.abspath("./images/bush.png")).convert_alpha()
        self.image_rock = pg.image.load(os.path.abspath("./images/rock.png")).convert_alpha()
        self.image_trunk = pg.image.load(os.path.abspath("./images/trunk.png")).convert_alpha()
        self.image_tree = pg.image.load(os.path.abspath("./images/tree.png")).convert_alpha()

        self.images_obstacles = {
            1: self.image_bush,  # Vers le haut (direction y négative)
            2: self.image_rock,  # Vers le bas (direction y positive)
            3: self.image_trunk,  # Vers la gauche (direction x négative)
            4: self.image_tree,  # Vers la droite (direction x positive)
        }


    def add_random_obstacles(self, line):
        if self.tableau[line][1].type_terrain == TypeTerrain.GRASS:
            for x in range(1, 13):
                if random.randint(1,10) in range(8): #permet de tirer 70% du temps un obstacle
                    self.tableau[line][x].obstacle = random.randint(1, 4)

        
    def create_random_line(self):
        terrain_aleatoire = random.choice([TypeTerrain.GRASS, TypeTerrain.GRASS, TypeTerrain.GRASS, TypeTerrain.ROAD, TypeTerrain.ROAD])
        return [Cell(TypeTerrain.GLITCH) if i in [0, 13] else Cell(terrain_aleatoire) for i in range(14)]
    
    def init_terrain(self):
        for y in range(20):
            self.tableau[y] = self.create_random_line()
            self.add_random_obstacles(y)
    

    def shift_terrain(self,screen):
        for y in range(18, -1, -1):
            for x in range(1, 13):
                self.tableau[y + 1][x] = self.tableau[y][x]

        # for i in range(20):
        #     print("___________________________________________________________________")
        #     for j in range(1, 13):
        #         print("Type :", self.tableau[i][j].type_terrain, "Obstacle :", self.tableau[i][j].obstacle)
    
    def draw_grass(self, screen, y):
        pg.draw.rect(screen, (117, 214, 112), (40, y * 40, 12 * 40, 40))

        for x in range(1, 13):
            if self.tableau[y][x].obstacle:
                # Récupérez l'image d'obstacle correspondante à partir du dictionnaire
                obstacle_image = self.images_obstacles.get(self.tableau[y][x].obstacle, None)
                
                if obstacle_image:
                    # Dessinez l'image d'obstacle sur l'écran
                    screen.blit(obstacle_image, (x * 40, y * 40))
        
        # for x in range(1, 13):
        #     if self.tableau[y][x].obstacle:
        #         self.tableau[y][x].obstacle.update(screen, (self.tableau[y][x].obstacle.x, self.tableau[y][x].obstacle.y))

    def draw_road(self, screen, y):
        pg.draw.rect(screen, (100, 100, 100), (40, y * 40, 12 * 40, 40))

    def update(self, screen):
        # draw the obstacles
        for y in range(20):
            if self.tableau[y][1].type_terrain == TypeTerrain.GRASS:
                self.draw_grass(screen, y)    
            elif self.tableau[y][1].type_terrain == TypeTerrain.ROAD:
                self.draw_road(screen, y)
        

            
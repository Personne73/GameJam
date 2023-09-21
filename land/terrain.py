import random
import pygame as pg
from enum import Enum
import os



class Obstacle(pg.sprite.Sprite):
    def __init__(self, x, y, obstacle_image):
        super(Obstacle, self).__init__()
        self.x = x
        self.y = y

        # Load the image, preserve alpha channel for transparency
        self.surf = pg.image.load(obstacle_image).convert_alpha()

        # Save the rect so you can move it
        self.rect = self.surf.get_rect()

    def update(self, screen, pos):
        '''
        pos : Tuple
        '''
        self.rect = pos

        # draw the image in the screen
        screen.blit(self.surf, self.rect)

class Bush(Obstacle):
    def __init__(self, x, y):
        self.bush = os.path.abspath("./images/bush.png")
        super().__init__(x, y, self.bush)

class Rock(Obstacle):
    def __init__(self, x, y):
        self.rock_image = os.path.abspath("./images/rock.png")
        super().__init__(x, y, self.rock_image)

class TreeTrunk(Obstacle):
    def __init__(self, x, y):
        self.tree_trunk_image = os.path.abspath("./images/trunk.png")
        super().__init__(x, y, self.tree_trunk_image)

class Tree(Obstacle):
    def __init__(self, x, y):
        self.tree_image = os.path.abspath("./images/tree.png")
        super().__init__(x, y, self.tree_image)

class Road():
    def __init__(self) -> None:
        self.sens

class TypeTerrain(Enum):
    GRASS = 1
    #WATER = 2
    ROAD = 2
    GLITCH = 3

class Cell():
    def __init__(self, type_terrain, obstacle=False):
        self.type_terrain = type_terrain
        self.obstacle = obstacle

class Terrain(object):
    # 20x14 blocks, dont 2 de bordure en largeur

    def __init__(self):
        self.tableau = [[]for j in range(20)]
        self.init_terrain()
        for i in range(20):
            for j in range(1, 13):
                print("Type :", self.tableau[i][j].type_terrain, "Obstacle :", self.tableau[i][j].obstacle)
        #self.init_terrain()

    def add_random_obstacles(self, line):
        obstacles = [Tree(0, 0), Bush(0,0), Rock(0,0), TreeTrunk(0, 0)]
        if self.tableau[line][1].type_terrain == TypeTerrain.GRASS:
            for x in range(1, 13):
                if random.randint(1,10) in range(8): #permet de tirer 70% du temps un obstacle
                    self.tableau[line][x].obstacle = random.choice(obstacles)
                    self.tableau[line][x].obstacle.x = x * 40
                    self.tableau[line][x].obstacle.y = line * 40

        
    def create_random_line(self):
        terrain_aleatoire = random.choice([TypeTerrain.GRASS, TypeTerrain.GRASS, TypeTerrain.GRASS, TypeTerrain.ROAD, TypeTerrain.ROAD])
        return [Cell(TypeTerrain.GLITCH) if i in [0, 13] else Cell(terrain_aleatoire) for i in range(14)]
    
    def init_terrain(self):
        for y in range(20):
            self.tableau[y] = self.create_random_line()
            self.add_random_obstacles(y)
    

    # def shift_terrain(self):
    #     for
    
        #     from obstacle.tree import Tree
        # from obstacle.bush import Bush
        # from obstacle.rock import Rock
        # from obstacle.tree_trunk import TreeTrunk

        # obstacle_list = [0 if i in [0, 13] else None for i in range(14)]
        # obstacles = [Tree(0, 0), Bush(0,0), Rock(0,0), TreeTrunk(0, 0)]
        # for i in range(1, 13):
        #     if random.randint(0, 4) in [0, 1, 2]:
        #         obstacle_list[i] = random.choice(obstacles)
        #         obstacle_list[i].x = i * 40
        #         obstacle_list[i].y = y * 40
        # return obstacle_list

    def draw_grass(self, screen, y):
        pg.draw.rect(screen, (117, 214, 112), (40, y * 40, 12 * 40, 40))
        
        for x in range(1, 13):
            if self.tableau[y][x].obstacle != False:
                self.tableau[y][x].obstacle.update(screen, (self.tableau[y][x].obstacle.x, self.tableau[y][x].obstacle.y))

    def draw_road(self, screen, y):
        pg.draw.rect(screen, (100, 100, 100), (40, y * 40, 12 * 40, 40))

    def update(self, screen):
        # draw the obstacles
        for y in range(20):
            if self.tableau[y][1].type_terrain == TypeTerrain.GRASS:
                self.draw_grass(screen, y)    
            elif self.tableau[y][1].type_terrain == TypeTerrain.ROAD:
                self.draw_road(screen, y)

        #print("\n")
            
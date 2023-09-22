import random
import pygame as pg
from enum import Enum
import os
import constants as const
from land.road import Road
from player import Buffer

class TypeTerrain(Enum):
    GRASS = 1
    ROAD = 2
    BLACK = 3
    GLITCH = 4

class Cell():
    def __init__(self, type_terrain, obstacle=0):
        self.type_terrain = type_terrain
        self.obstacle = obstacle

class Terrain(object):
    # 20x14 blocks, dont 2 de bordure en largeur
    buffer_y = Buffer(const.CASE_SIZE / const.MOVE_STEPS)
    px_y = 0

    def __init__(self):
        self.tableau = [[]] * (const.HEIGHT + 1)

        self.init_terrain()

        self.image_bush = pg.image.load(os.path.abspath("./images/bush.png")).convert_alpha()
        self.image_rock = pg.image.load(os.path.abspath("./images/rock.png")).convert_alpha()
        self.image_trunk = pg.image.load(os.path.abspath("./images/trunk.png")).convert_alpha()
        self.image_tree = pg.image.load(os.path.abspath("./images/tree.png")).convert_alpha()

        self.images_obstacles = {
            1: self.image_bush,  
            2: self.image_rock,  
            3: self.image_trunk,  
            4: self.image_tree, 
        }

        self.count_lines = 0

        self.bloc_glitch = [[Cell(TypeTerrain.BLACK), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.BLACK)],
                            [Cell(TypeTerrain.GLITCH), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GLITCH)],
                            [Cell(TypeTerrain.GLITCH), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GLITCH)],
                            [Cell(TypeTerrain.GLITCH), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GLITCH)],
                            [Cell(TypeTerrain.GLITCH), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GLITCH)],
                            [Cell(TypeTerrain.GLITCH), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, random.randint(1,4)), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GRASS, 0), Cell(TypeTerrain.GLITCH)],
                            [Cell(TypeTerrain.BLACK), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.GRASS), Cell(TypeTerrain.BLACK)]
                            ]
        self.count_bloc_glitch = 6
        
    def add_random_obstacles(self, line):
        if self.tableau[line][1].type_terrain == TypeTerrain.GRASS:

            max_obstacle = 8
            count = 0
        
            for x in range(1, 13):
                if random.randint(1,10) in range(6) and count <= max_obstacle: #permet de tirer 70% du temps un obstacle
                    self.tableau[line][x].obstacle = random.randint(1, 4)
                    count += 1
            
            if(line == 20):
                return

            # check if first grass line
            if(self.tableau[line+1][1].type_terrain == TypeTerrain.GRASS):
                for x in range(1, 13):
                    if(self.tableau[line +1][x].obstacle == 0):
                        self.tableau[line][x].obstacle = 0


    def create_random_line(self):
        terrain_aleatoire = random.choice([TypeTerrain.GRASS, TypeTerrain.GRASS, TypeTerrain.GRASS, TypeTerrain.ROAD, TypeTerrain.ROAD])
        new_line = [Cell(TypeTerrain.BLACK) if i in [0, 13] else Cell(terrain_aleatoire) for i in range(14)]
        if terrain_aleatoire is TypeTerrain.ROAD:
            new_line[1] = Road(TypeTerrain.ROAD)
        return new_line
    
    def init_terrain(self):
        for y in range(20, -1, -1):
            self.tableau[y] = self.create_random_line()
            self.add_random_obstacles(y)
            if self.tableau[y][1].type_terrain is TypeTerrain.ROAD:
                self.tableau[y][1].move(y * const.CASE_SIZE)

        for i in range(const.HEIGHT - const.SCROLL_STOP):
            for x in range(1, 13):
                self.tableau[20 - i][x] = Cell(TypeTerrain.GRASS, 0)
    

    def shift_terrain(self):
        self.buffer_y.add(const.MOVE_STEPS)
        to_delete_line = self.tableau[len(self.tableau) - 1]
        if to_delete_line[1].type_terrain is TypeTerrain.ROAD:
            to_delete_line[1].kill()
        for y in range(19, -1, -1):
            for x in range(14):
                self.tableau[y + 1][x] = self.tableau[y][x]
        
        if (self.count_bloc_glitch != 6 or self.count_lines % 70 == 0) and self.count_lines != 0:
            self.tableau[0] = self.bloc_glitch[self.count_bloc_glitch]
            self.count_bloc_glitch -= 1
            if self.count_bloc_glitch == -1: self.count_bloc_glitch = 6
        else:
            self.tableau[0] = self.create_random_line()
            self.add_random_obstacles(0)
        self.count_lines += 1
        self.px_y += - const.CASE_SIZE
    
    def draw_grass(self, screen, y, px):
        pg.draw.rect(screen, (117, 214, 112), (40, px, 12 * 40, 40))

        for x in range(1, 13):
            if self.tableau[y][x].obstacle:
                # Récupérez l'image d'obstacle correspondante à partir du dictionnaire
                obstacle_image = self.images_obstacles.get(self.tableau[y][x].obstacle, None)
                
                if obstacle_image:
                    # Dessinez l'image d'obstacle sur l'écran
                    screen.blit(obstacle_image, (x * 40, px))

    def draw_road(self, screen, px):
        pg.draw.rect(screen, (100, 100, 100), (40, px, 12 * 40, 40))
    
    def draw_road_marks(self, screen, px):
        road_marks = pg.image.load(os.path.abspath("./images/road_marks.png")).convert_alpha()
        screen.blit(road_marks, (40, px))

    def update(self, screen, car_group):
        self.px_y += self.buffer_y.consume()
        # draw the obstacles
        for y in range(len(self.tableau)):
            px = y * const.CASE_SIZE + self.px_y
            if self.tableau[y][1].type_terrain == TypeTerrain.GRASS:
                self.draw_grass(screen, y, px)    
            elif self.tableau[y][1].type_terrain == TypeTerrain.ROAD:
                self.draw_road(screen, px)

                #check if lane road lane is size >= 2 to draw road marks:
                if y > 0 and self.tableau[y-1][1].type_terrain == TypeTerrain.ROAD:
                    self.draw_road_marks(screen, px)

                road = self.tableau[y][1]
                road.update(car_group)
                if (road.y != px):
                    road.move(px)

            
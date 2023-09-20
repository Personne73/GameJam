import random
import pygame as pg


class Terrain(object):
    # 20x14 blocks, dont 2 de bordure en largeur

    def __init__(self):
        self.tableau = [[0 if i in [0, 13] else None for i in range(14)] for j in range(20)]
        self.init_terrain()

    def add_random_line_obstacle(self, y):
        from obstacle.tree import Tree
        from obstacle.bush import Bush
        from obstacle.rock import Rock
        from obstacle.tree_trunk import TreeTrunk

        obstacle_list = [0 if i in [0, 13] else None for i in range(14)]
        obstacles = [Tree(0, 0), Bush(0,0), Rock(0,0), TreeTrunk(0, 0)]
        for i in range(1, 13):
            if random.randint(0, 4) in [0, 1, 2]:
                obstacle_list[i] = random.choice(obstacles)
                obstacle_list[i].x = i * 40
                obstacle_list[i].y = y * 40
        return obstacle_list

    def init_terrain(self):
        for i in range(1):
            self.tableau[i] = self.add_random_line_obstacle(i)

    def update(self, screen):
        # draw the obstacles
        for i in range(1):
            for j in range(1, 13):
                #print(self.tableau[i][j], end=" ")
                pg.draw.rect(screen, (117, 214, 112), (40, i * 40, 12 * 40, 40))
                if self.tableau[i][j] is not None:
                    #print("(", self.tableau[i][j].x, self.tableau[i][j].y, ")", end=" ")
                        #self.obstacle_list[i] = self.obstacle_list[i](40 + i * 40, row_index * 40)
                    self.tableau[i][j].update(screen, (self.tableau[i][j].x, self.tableau[i][j].y))
            #print("\n")
            
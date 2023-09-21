# import pygame as pg
# import random


# class Row(object):
#     HEIGHT = 40
#     WIDTH = 480

#     def __init__(self, type):
#         self.obstacle_list = [0 if i in [0, 13] else None for i in range(14)]
#         #self.add_random_obstacle()
#         self.type = type

#     def add_random_obstacle(self):
#         from obstacle.tree import Tree
#         from obstacle.bush import Bush
#         from obstacle.rock import Rock
#         from obstacle.tree_trunk import TreeTrunk

#         obstacles = [Tree(0, 0), Bush(0,0), Rock(0,0), TreeTrunk(0, 0)]
#         for i in range(1, 13):
#             if random.randint(0, 4) in [0, 1, 2]:
#                 self.obstacle_list[i] = random.choice(obstacles)
#                 self.obstacle_list[i].x = i * 40

#     def update(self, screen, row_index):
#         if self.type == "grass":
#             grass_color = (117, 214, 112)
#             pg.draw.rect(screen, grass_color, (40, row_index*40, Row.WIDTH, Row.HEIGHT))

#             # draw the obstacles
#             for i in range(20):
#                 for j in range(1, 13):
#                     if self.obstacle_list[i][j] is not None:
#                         #self.obstacle_list[i] = self.obstacle_list[i](40 + i * 40, row_index * 40)
#                         self.obstacle_list[i][j].update(screen, self.obstacle_list[i][j].x, self.obstacle_list[i][j].y)



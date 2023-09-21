import pygame as pg
import sys

from land.row import Row
from land.terrain import Terrain
from obstacle.bush import Bush
from obstacle.rock import Rock
from obstacle.tree import Tree
from obstacle.tree_trunk import TreeTrunk
from obstacle.void import Void

FRAMERATE = 60 # Set fps


def main():
    pg.init()
    window_size = (560, 800)
    screen = pg.display.set_mode(window_size)
    game_over = False

    #tree = Tree(0, 0)
    #bush = Bush(window_size[0] / 2, window_size[1] / 2)
    #rock = Rock(100, 100)
    #trunk = TreeTrunk(200, 200)
    #void = Void(window_size[0] / 2, window_size[1] / 2)
    #grass = Row("grass")
    terrain = Terrain()

    clock_framerate = pg.time.Clock()
    while not game_over:
        # draw a rect in the middle of the screen
        # pg.draw.rect(screen, (255, 0, 0), (window_size[0] / 2 - 50, window_size[1] / 2 - 50, 100, 100))
        # screen.blit(tree_image, (tree.x, tree.y))
        # grass.update(screen, 0)
        # bush.update(screen, (bush.x, bush.y))
        # tree.update(screen, (tree.x, tree.y))
        # rock.update(screen, (rock.x, rock.y))
        # trunk.update(screen, (trunk.x, trunk.y))
        # void.update(screen, (void.x, void.y))
        terrain.update(screen)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    game_over = True

        clock_framerate.tick(FRAMERATE)
        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()
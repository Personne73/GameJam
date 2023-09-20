import pygame as pg
import pygame.draw
import sys

from obstacle.tree import Tree

FRAMERATE = 60 # Set fps

def main():
    pg.init()
    window_size = (560, 800)
    screen = pg.display.set_mode(window_size)
    game_over = False

    tree_image = r".\images\tree.png"
    tree = Tree(window_size[0] / 2, window_size[1] / 2, tree_image)

    clock_framerate = pg.time.Clock()
    while not game_over:
        # draw a rect in the middle of the screen
        # pg.draw.rect(screen, (255, 0, 0), (window_size[0] / 2 - 50, window_size[1] / 2 - 50, 100, 100))
        # screen.blit(tree_image, (tree.x, tree.y))
        tree.update(screen, (tree.x, tree.y))

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
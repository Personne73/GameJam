import pygame as pg
import sys

from land.terrain import Terrain

FRAMERATE = 60 # Set fps


def main():
    pg.init()
    window_size = (560, 800)
    screen = pg.display.set_mode(window_size)
    game_over = False
    terrain = Terrain()

    clock_framerate = pg.time.Clock()
    while not game_over:
        terrain.update(screen)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    game_over = True
                if event.key == pg.K_z:
                    terrain.shift_terrain(screen)

        clock_framerate.tick(FRAMERATE)
        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()
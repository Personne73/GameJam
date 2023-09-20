import pygame as pg
import sys

from land.terrain import Terrain
from player import Player

FRAMERATE = 60 # Set fps
CASE_SIZE = 40 #pixels
WIDTH = 14
HEIGHT = 20
WINDOW_SIZE = (CASE_SIZE * WIDTH, CASE_SIZE * HEIGHT)


def main():
    pg.init()
    screen = pg.display.set_mode(WINDOW_SIZE)
    game_over = False
    terrain = Terrain()
    
    clock_framerate = pg.time.Clock()
    player = Player()
    
    while not game_over:
        terrain.update(screen)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    game_over = True
                elif event.key == pg.K_z:
                    player.move(0, 1)
                    terrain.shift_terrain(screen)
                elif event.key == pg.K_s:
                    player.move(0, -1)
                elif event.key == pg.K_d:
                    player.move(1, 0)
                elif event.key == pg.K_q:
                    player.move(-1, 0)
        
        screen.fill("#b1d670")
        player.draw(screen)
        pg.display.flip()
        clock_framerate.tick(FRAMERATE)
    pg.quit()


if __name__ == "__main__":
    main()
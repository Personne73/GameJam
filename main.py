import pygame as pg
import sys

from land.terrain import Terrain
import player as pl
from land.road import Road
from pathlib import Path

FRAMERATE = 60 # Set fps
CASE_SIZE = 40 #pixels
WIDTH = 14
HEIGHT = 20
WINDOW_SIZE = (CASE_SIZE * WIDTH, CASE_SIZE * HEIGHT)


def main():
    pg.init()
    screen = pg.display.set_mode(WINDOW_SIZE)
    
    game_over = False
    clock_framerate = pg.time.Clock()
    terrain = Terrain()

    player = pl.Player(str(Path.cwd()) + "/Sprites/")
    player_group = pg.sprite.Group()
    player_group.add(player)

    car_group = pg.sprite.Group()
    road1 = Road(str(Path.cwd()) + "/Sprites/")
    road2 = Road(str(Path.cwd()) + "/Sprites/")
    road3 = Road(str(Path.cwd()) + "/Sprites/")
    road2.move(CASE_SIZE)
    road3.move(CASE_SIZE * 3)

    while not game_over and player.is_alive:
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
        player_group.draw(screen)
        player_group.update(car_group)
        car_group.draw(screen)
        car_group.update(0.05)
        road1.update(car_group)
        road2.update(car_group)
        road3.update(car_group)
        pg.display.update()
        clock_framerate.tick(FRAMERATE)
    pg.quit()


if __name__ == "__main__":
    main()
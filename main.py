import pygame as pg
import sys

from land.terrain import Terrain
from land.terrain import TypeTerrain
import player as pl
import constants

MASK_L = pg.Rect(0, 0, constants.CASE_SIZE, constants.CASE_SIZE * constants.HEIGHT)
MASK_R = pg.Rect(constants.CASE_SIZE * (constants.WIDTH - 1), 0, constants.CASE_SIZE, constants.CASE_SIZE * constants.HEIGHT)

def draw_score(score, best_score, screen):
    if score >= best_score:
        best_score = score

    #font sizes
    SMALL_FONT = 15
    MEDIUM_FONT = 15
    BIG_FONT = 25

    #font decalarations
    crossy_font_big = pg.font.Font('font/8-BIT WONDER.TTF', BIG_FONT)
    crossy_font_small = pg.font.Font('font/8-BIT WONDER.TTF', SMALL_FONT)

    my_score = crossy_font_big.render(str(score), True, 'white')
    my_best_score = crossy_font_small.render('TOP ' + str(best_score), True, 'white')

    #affichage des scores
    CORNER = 40
    screen.blit(my_score, (CORNER + 10, 10))

    if not best_score == None:
        screen.blit(my_best_score, (CORNER + 10, CORNER + 10))

def encounter_obstacle(player_pos, terrain, direction):
    pos_x = player_pos[0] + direction[0]
    pos_y = player_pos[1] + direction[1]
    if terrain[pos_y][pos_x].type_terrain == TypeTerrain.GLITCH:
        return False
    if pos_y >= len(terrain) or pos_x >= len(terrain[0]) or terrain[pos_y][pos_x].obstacle != 0 or terrain[pos_y][pos_x].type_terrain == TypeTerrain.BLACK:
        return True
    return False



def main():
    pg.init()
    screen = pg.display.set_mode(constants.WINDOW_SIZE)
    
    game_over = False
    clock_framerate = pg.time.Clock()
    terrain = Terrain()

    score = 0
    best_score = 0

    player = pl.Player(constants.IMG_PATH)
    player_group = pg.sprite.Group()
    player_group.add(player)

    car_group = pg.sprite.Group()

    while not game_over and player.is_alive:
        terrain.update(screen, car_group)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    game_over = True
                elif event.key == pg.K_z:
                    obstacle = encounter_obstacle(player.get_position(), terrain.tableau, (0, -1))
                    if not obstacle and player.get_position()[1] <= player.SCROLL_STOP:
                        score += 1
                        terrain.shift_terrain()
                    player.move(0, 1, obstacle)
                elif event.key == pg.K_s:
                    player.move(0, -1, encounter_obstacle(player.get_position(), terrain.tableau, (0, 1)))
                elif event.key == pg.K_d:
                    player.move(1, 0, encounter_obstacle(player.get_position(), terrain.tableau, (1, 0)))
                elif event.key == pg.K_q:
                    player.move(-1, 0, encounter_obstacle(player.get_position(), terrain.tableau, (-1, 0)))
    
        player_group.update(car_group)
        car_group.update(0.05)
        car_group.draw(screen)
        draw_mask(screen)
        player_group.draw(screen)
        draw_score(score, best_score, screen)
        pg.display.update()
        clock_framerate.tick(constants.FRAMERATE)
    pg.quit()

def draw_mask(screen):
    pg.draw.rect(screen, "black", MASK_L)
    pg.draw.rect(screen, "black", MASK_R)


if __name__ == "__main__":
    main()
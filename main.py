import pygame as pg

FRAMERATE = 60 # Set fps

def main():
    pg.init()
    window_size = (560, 800)
    screen = pg.display.set_mode(window_size)
    game_over = False
    
    clock_framerate = pg.time.Clock()

    while not game_over:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    game_over = True
        
        clock_framerate.tick(FRAMERATE)

    pg.quit()


if __name__ == "__main__":
    main()
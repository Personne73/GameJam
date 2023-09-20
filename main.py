import pygame as pg

FRAMERATE = 60 # Set fps

def main():
    pg.init()
    windowSize = (1000, 800)
    screen = pg.display.set_mode(windowSize)
    GameOver = False
    
    clockFramerate = pg.time.Clock()

    while not GameOver:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    GameOver = True
        
        clockFramerate.tick(FRAMERATE)

    pg.quit()


if __name__ == "__main__":
    main()
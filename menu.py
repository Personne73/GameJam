import pygame as pg

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.font = pg.font.Font(None, 36)
        self.start_button = pg.Rect(self.width // 4, self.height // 2 - 50, self.width // 2, 50)
        self.high_score_button = pg.Rect(self.width // 4, self.height // 2 + 50, self.width // 2, 50)

    def draw(self):
        # Dessiner le fond du menu
        self.screen.fill((0, 0, 0))  # Couleur de fond (noir)

        # Dessiner le bouton "Start"
        pg.draw.rect(self.screen, (0, 255, 0), self.start_button)
        start_text = self.font.render("Start", True, (0, 0, 0))
        start_text_rect = start_text.get_rect(center=self.start_button.center)
        self.screen.blit(start_text, start_text_rect)

        # Dessiner le bouton "High Score"
        pg.draw.rect(self.screen, (0, 255, 0), self.high_score_button)
        high_score_text = self.font.render("High Score", True, (0, 0, 0))
        high_score_text_rect = high_score_text.get_rect(center=self.high_score_button.center)
        self.screen.blit(high_score_text, high_score_text_rect)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic gauche de la souris
                    if self.start_button.collidepoint(event.pos):
                        print("Start button clicked")  # Vous pouvez ajouter le code de démarrage du jeu ici
                    elif self.high_score_button.collidepoint(event.pos):
                        print("High Score button clicked")  # Vous pouvez ajouter le code pour afficher les scores ici

def main():
    pg.init()
    window_size = (800, 600)
    screen = pg.display.set_mode(window_size)
    game_over = False
    
    clock_framerate = pg.time.Clock()
    menu = Menu(screen)

    while not game_over:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    game_over = True
        
        menu.handle_events()
        menu.draw()

        pg.display.flip()
        clock_framerate.tick(60)

    pg.quit()

if __name__ == "__main__":
    main()
